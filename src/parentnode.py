from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props={}):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self, html_builder=""):
        if self.tag is None:
            raise ValueError("Please Provide a Tag")
        if not self.children:
            raise ValueError("Parent Nodes must have children.")
        for child in self.children:
            html_builder += child.to_html()
        return f"<{self.tag}>{html_builder}</{self.tag}>"
