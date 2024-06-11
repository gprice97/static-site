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

    def test_text_to_html(self):
        node = TextNode("This is Gunnar's Text", "image", "www.GunnarsHouse.com")
        self.assertEqual(node.text_node_to_html_node(),
                         LeafNode('img', "",  {'src': 'www.GunnarsHouse.com', 'alt': "This is Gunnar's Text"}))


if __name__ == "__main__":
    unittest.main()
