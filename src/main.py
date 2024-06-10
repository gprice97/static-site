from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
    new_node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(new_node.__repr__())
    node_2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(node_2.props_to_html())
    node_3 = LeafNode("p", "This is a paragraph of text.")
    print(node_3.to_html())
    node_4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(node_4.to_html())


main()
