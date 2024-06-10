import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
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
        self.assertEqual(node_5.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_2(self):
        node_6 = ParentNode(
            "h1", [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
            ]
        )

        print(node_6.to_html())
        self.assertEqual(node_6.to_html(), '<h1><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></h1>')


if __name__ == "__main__":
    unittest.main()
