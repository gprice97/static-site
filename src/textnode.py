from leafnode import LeafNode
import re


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = "" if url is None else url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url)
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self):
        if self.text_type == "text":
            return LeafNode(None, self.text)
        elif self.text_type == "bold":
            return LeafNode("b", self.text)
        elif self.text_type == "italic":
            return LeafNode("i", self.text)
        elif self.text_type == "code":
            return LeafNode("code", self.text)
        elif self.text_type == "link":
            return LeafNode("a", self.text, [], {"href": self.url})
        elif self.text_type == "image":
            return LeafNode("img", "", [], {"src": self.url, "alt": self.text})
        else:
            raise Exception("Not a valid TextNode")

    def split_nodes_delimiter(self, old_nodes, delimiter, new_text_type):
        # Create a List that will be returned containing New Nodes
        new_nodes = []

        # Begin searching through the list of the nodes
        for node in old_nodes:

            # Verify that the "node" currently being worked on is a TextNode
            if isinstance(node, TextNode):

                # Ensure there is an even number of delimiters
                if node.text.count(delimiter) % 2 != 0:
                    raise Exception("Provide a closing delimiter")

                # Split text at each delimiter
                string_list = node.text.split(delimiter)

                # Iterate through parts and construct new TextNodes
                for i in range(0, len(string_list)):
                    if i % 2 == 0:
                        # Plain text segments
                        new_nodes.append(TextNode(string_list[i], node.text_type))
                    else:
                        # Text segments between delimiters
                        new_nodes.append(TextNode(string_list[i], new_text_type, ))

            # If the Node Currently being worked on ISN'T a textnode, then we can just add it on as is.
            else:
                new_nodes.append(node)

        return new_nodes

    def extract_markdown_images(self):
        return re.findall(r"!\[(.*?)\]\((.*?)\)", self.text)

    def extract_markdown_links(self):
        return re.findall(r"\[(.*?)\]\((.*?)\)", self.text)

    def split_nodes_image(self, old_nodes):
        new_nodes = []
        for node in old_nodes:
            # For each of the nodes, I want to make sure they are images
            matched_images = re.findall(r'!\[([^\]]+)\]\(([^)]+)\)', node.text)
            # If there is an image in the text
            if matched_images:
                text = node.text
                # We work through each instance of an image in the text
                for alt_text, url in matched_images:
                    parts = text.split(f'![{alt_text}]({url})', 1)
                    if parts[0]:
                        new_nodes.append(TextNode(parts[0], "text_type_text"))
                    new_nodes.append(TextNode(alt_text, "text_type_image", url))
                    text = parts[1]
                if text:
                    new_nodes.append(TextNode(text, "text_type_text"))
            else:
                new_nodes.append(node)
        return new_nodes

    def split_nodes_link(self, old_nodes):
        new_nodes = []
        for node in old_nodes:
            # For each of the nodes, I want to make sure they are links
            matched_links = re.findall(r"\[(.*?)\]\((.*?)\)", node.text)
            # If there is a link in the text
            if matched_links:
                text = node.text
                # We work through each instance of a link in the text
                for link_text, url in matched_links:
                    parts = text.split(f'[{link_text}]({url})', 1)
                    if parts[0]:
                        new_nodes.append(TextNode(parts[0], "text_type_text"))
                    new_nodes.append(TextNode(link_text, "text_type_url", url))
                    text = parts[1]
                if text:
                    new_nodes.append(TextNode(text, "text_type_text"))
            else:
                new_nodes.append(node)
        return new_nodes
