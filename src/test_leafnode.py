import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        # Test 1: Verify props_to_html works as intended.
        node = LeafNode("a", "Click me!", [], {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

        # Test 2: Verify empty HTML Node returns an empty string
        node_2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node_2.to_html(), '<p>This is a paragraph of text.</p>')


if __name__ == "__main__":
    unittest.main()
