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

    def test_text_extract_links_1(self):
        node = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", "text", None)
        actual_link = node.extract_markdown_links()
        expected_link = [('link', 'https://www.example.com'), ('another', 'https://www.example.com/another')]
        self.assertEqual(actual_link, expected_link, f"Values do not match!\nExpected: {expected_link}\nActual: {actual_link}")

    def test_text_extract_images_1(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)",
            "text", None)
        actual_image = node.extract_markdown_links()
        expected_image = [('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')]
        self.assertEqual(actual_image, expected_image, f"Values do not match!\nExpected: {expected_image}\nActual: {actual_image}")

    def test_split_image_1(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text", None)
        actual_nodes = node.split_nodes_image([node])
        expected_nodes = [TextNode('This is text with an ', 'text_type_text', ),
                          TextNode('image', 'text_type_image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'),
                          TextNode(' and another ', 'text_type_text', ),
                          TextNode('second image', 'text_type_image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png')]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")

    def test_split_image_2(self):
        node = TextNode("This is text", "text", None)
        actual_nodes = node.split_nodes_image([node])
        expected_nodes = [TextNode('This is text', 'text', )]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")

    def test_split_image_3(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)",
            "text", None)
        actual_nodes = node.split_nodes_image([node])
        expected_nodes = [TextNode('This is text with an ', 'text_type_text', ),
                          TextNode('image', 'text_type_image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png')]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")

    def test_split_image_4(self):
        node = TextNode(
            "![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) Shown above is the image of a Lion on the prowl not to be confused with the image below of a penguin ![image](https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTlHcpgBeZ4jAHIxBi5VMDbTSpQfoyKyAVIM3NJ19H60jWfrjMGbUlzRulBc2Mhu2eK) Or the following image of a Tambourine! ![image](https://m.media-amazon.com/images/I/81OBNvoVk6L.jpg)",
            "text", None)
        actual_nodes = node.split_nodes_image([node])
        expected_nodes = [TextNode('image', 'text_type_image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'),
                          TextNode(' Shown above is the image of a Lion on the prowl not to be confused with the image below of a penguin ', 'text_type_text', ),
                          TextNode('image', 'text_type_image', 'https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTlHcpgBeZ4jAHIxBi5VMDbTSpQfoyKyAVIM3NJ19H60jWfrjMGbUlzRulBc2Mhu2eK'),
                          TextNode(' Or the following image of a Tambourine! ', 'text_type_text', ),
                          TextNode('image', 'text_type_image', 'https://m.media-amazon.com/images/I/81OBNvoVk6L.jpg')]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")


    def test_split_image_5(self):
        node = TextNode("", "text", None)
        actual_nodes = node.split_nodes_image([node])
        expected_nodes = [TextNode('', 'text', )]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")


    def test_split_link_1(self):
        node = TextNode(
            "This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text", None)
        actual_nodes = node.split_nodes_link([node])
        expected_nodes = [TextNode('This is text with an ', 'text_type_text', ),
                          TextNode('link', 'text_type_url', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'),
                          TextNode(' and another ', 'text_type_text', ),
                          TextNode('second link', 'text_type_url', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png')]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")

    def test_split_link_2(self):
        node = TextNode(
            "This is text with no link",
            "text", None)
        actual_nodes = node.split_nodes_link([node])
        expected_nodes = [TextNode('This is text with no link', 'text', ),]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")

    def test_split_link_3(self):
        node = TextNode(
            "[link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) Shown above a link to a Lion on the prowl not to be confused with the link below leading to a penguin [link](https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTlHcpgBeZ4jAHIxBi5VMDbTSpQfoyKyAVIM3NJ19H60jWfrjMGbUlzRulBc2Mhu2eK) Or the following link to a Tambourine! [link](https://m.media-amazon.com/images/I/81OBNvoVk6L.jpg)",
            "text", None)
        actual_nodes = node.split_nodes_link([node])
        expected_nodes = [TextNode('link', 'text_type_url', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'),
                          TextNode(' Shown above a link to a Lion on the prowl not to be confused with the link below leading to a penguin ', 'text_type_text', ),
                          TextNode('link', 'text_type_url', 'https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTlHcpgBeZ4jAHIxBi5VMDbTSpQfoyKyAVIM3NJ19H60jWfrjMGbUlzRulBc2Mhu2eK'),
                          TextNode(' Or the following link to a Tambourine! ', 'text_type_text', ),
                          TextNode('link', 'text_type_url', 'https://m.media-amazon.com/images/I/81OBNvoVk6L.jpg')]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")

    def test_split_link_4(self):
        node = TextNode(
            "",
            "text", None)
        actual_nodes = node.split_nodes_link([node])
        expected_nodes = [TextNode('', 'text', ),]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")

    def test_split_link_5(self):
        node = TextNode(
            "This is text with one link [link](www.totallycoollinks.com)",
            "text", None)
        actual_nodes = node.split_nodes_link([node])
        expected_nodes = [TextNode('This is text with one link ', 'text_type_text', ),
                          TextNode('link', 'text_type_url', 'www.totallycoollinks.com')]
        self.assertEqual(actual_nodes, expected_nodes, f"Values do not match!\nExpected: {expected_nodes}\nActual: {actual_nodes}")


if __name__ == "__main__":
    unittest.main()
