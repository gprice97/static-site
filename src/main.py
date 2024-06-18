from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    new_node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(new_node.__repr__())
    node_2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(node_2.props_to_html())
    node_3 = LeafNode("p", "This is a paragraph of text.")
    print(node_3.to_html())
    node_4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(node_4.to_html())
    node_5 = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    print(node_5.to_html())
    node_6 = TextNode("This is Gunnar's Text", "image", "www.GunnarsHouse.com")
    print(node_6.text_node_to_html_node())

    node_7 = TextNode("This is text with a `code block` word", "text", None)
    new_nodes = node_7.split_nodes_delimiter([node_7], "`", "code")
    print(new_nodes)

    node_8 = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", "text", None)
    print(node_8.extract_markdown_links())

    node_9 = TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)", "text", None)
    print(node_9.extract_markdown_images())


main()
