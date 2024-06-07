from textnode import TextNode
from htmlnode import HTMLNode


def main():
    new_node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(new_node.__repr__())
    node_2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(node_2.props_to_html())


main()
