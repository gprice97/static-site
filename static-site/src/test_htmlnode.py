import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        # Test 1: Verify props_to_html works as intended.
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

        # Test 2: Verify empty HTML Node returns an empty string
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node2.props_to_html(), '')

    def test_repr(self):
        # Test 1: Verify __repr__ works as intended.
        node = HTMLNode("p", "This is my paragraph text", [], {"p": "This is my paragraph text"})
        self.assertEqual(node.__repr__(), 'HTMLNode(p, This is my paragraph text, [], {\'p\': \'This is my paragraph text\'})')


if __name__ == "__main__":
    unittest.main()
