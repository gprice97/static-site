import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", 'https://boot.dev')
        node2 = TextNode("This is a text node", "bold", 'https://boot.dev')
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "italics", 'www.youtube.com')
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, italics, www.youtube.com)")


if __name__ == "__main__":
    unittest.main()
