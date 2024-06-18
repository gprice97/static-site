import unittest

from textnode import TextNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", 'https://boot.dev')
        node2 = TextNode("This is a text node", "bold", 'https://boot.dev')
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "italics", 'www.youtube.com')
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, italics, www.youtube.com)")

    def test_text_to_html_image(self):
        result = TextNode("This is Gunnar's Text", "image", "www.GunnarsHouse.com").text_node_to_html_node()
        expected = LeafNode('img', "", [],  {'src': "www.GunnarsHouse.com", 'alt': "This is Gunnar's Text"})
        self.assertEqual(result.tag, expected.tag, f"Tags do not match: {result.tag} != {expected.tag}")
        self.assertEqual(result.value, expected.value, f"Values do not match: {result.value} != {expected.value}")
        self.assertEqual(result.children, expected.children, f"Children do not match: {result.children} != {expected.children}")
        self.assertEqual(result.props, expected.props, f"Props do not match: {result.props} != {expected.props}")

    def test_text_to_html_link(self):
        result = TextNode("This is my anchor text", "link", "www.interestinglink.com").text_node_to_html_node()
        expected = LeafNode('a', "This is my anchor text", [],  {'href': "www.interestinglink.com"})
        self.assertEqual(result.tag, expected.tag, f"Tags do not match: {result.tag} != {expected.tag}")
        self.assertEqual(result.value, expected.value, f"Values do not match: {result.value} != {expected.value}")
        self.assertEqual(result.children, expected.children, f"Children do not match: {result.children} != {expected.children}")
        self.assertEqual(result.props, expected.props, f"Props do not match: {result.props} != {expected.props}")

    def test_text_to_html_text(self):
        result = TextNode("New Text 1235@512", "text", "").text_node_to_html_node()
        expected = LeafNode(None, "New Text 1235@512", [],  {})
        self.assertEqual(result.tag, expected.tag, f"Tags do not match: {result.tag} != {expected.tag}")
        self.assertEqual(result.value, expected.value, f"Values do not match: {result.value} != {expected.value}")
        self.assertEqual(result.children, expected.children, f"Children do not match: {result.children} != {expected.children}")
        self.assertEqual(result.props, expected.props, f"Props do not match: {result.props} != {expected.props}")

    def test_text_to_html_bold(self):
        result = TextNode("Emboldened, the Humans of Stormwind", "bold", "").text_node_to_html_node()
        expected = LeafNode("b", "Emboldened, the Humans of Stormwind", [],  {})
        self.assertEqual(result.tag, expected.tag, f"Tags do not match: {result.tag} != {expected.tag}")
        self.assertEqual(result.value, expected.value, f"Values do not match: {result.value} != {expected.value}")
        self.assertEqual(result.children, expected.children, f"Children do not match: {result.children} != {expected.children}")
        self.assertEqual(result.props, expected.props, f"Props do not match: {result.props} != {expected.props}")

    def test_text_to_html_italic(self):
        result = TextNode("Want to drink Diet soda and play PS2?", "italic", "").text_node_to_html_node()
        expected = LeafNode("i", "Want to drink Diet soda and play PS2?", [],  {})
        self.assertEqual(result.tag, expected.tag, f"Tags do not match: {result.tag} != {expected.tag}")
        self.assertEqual(result.value, expected.value, f"Values do not match: {result.value} != {expected.value}")
        self.assertEqual(result.children, expected.children, f"Children do not match: {result.children} != {expected.children}")
        self.assertEqual(result.props, expected.props, f"Props do not match: {result.props} != {expected.props}")

    def test_text_to_html_code(self):
        result = TextNode("if this code is the best then say yay", "code", "").text_node_to_html_node()
        expected = LeafNode("code", "if this code is the best then say yay", [],  {})
        self.assertEqual(result.tag, expected.tag, f"Tags do not match: {result.tag} != {expected.tag}")
        self.assertEqual(result.value, expected.value, f"Values do not match: {result.value} != {expected.value}")
        self.assertEqual(result.children, expected.children, f"Children do not match: {result.children} != {expected.children}")
        self.assertEqual(result.props, expected.props, f"Props do not match: {result.props} != {expected.props}")

    def test_split_nodes_delimiter_1(self):
        node = TextNode("This is text with a `code block` word", "text", None)
        real_node_list = [TextNode("This is text with a ", "text", ), TextNode("code block", "code", ), TextNode(" word", "text", )]
        new_nodes = node.split_nodes_delimiter([node], "`", "code")
        self.assertEqual(new_nodes, real_node_list, f"Nodes do not match!")

    def test_split_nodes_delimiter_2(self):
        node = TextNode("You guys ever seen the **DINO** Exhibit?!", "text", None)
        real_node_list = [TextNode("You guys ever seen the ", "text", None), TextNode("DINO", "bold", None), TextNode(" Exhibit?!", "text", None)]
        new_nodes = node.split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(new_nodes, real_node_list, f"Nodes do not match!")

    def test_split_nodes_delimiter_3(self):
        node = TextNode("You guys ever seen the *DINO* Exhibit?!", "text", None)
        real_node_list = [TextNode("You guys ever seen the ", "text", None), TextNode("DINO", "italics", None), TextNode(" Exhibit?!", "text", None)]
        new_nodes = node.split_nodes_delimiter([node], "*", "italics")
        self.assertEqual(new_nodes, real_node_list, f"Nodes do not match!")


if __name__ == "__main__":
    unittest.main()
