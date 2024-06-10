# This class will handle HTML nodes, thus far just printing a given Node by the values presented in the
# constructor.
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = [] if children is None else children
        self.props = {} if props is None else props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        string_builder = ""
        for prop in self.props:
            string_builder += f' {prop}="{self.props[prop]}"'
        return string_builder

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
