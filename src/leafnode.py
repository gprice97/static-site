from htmlnode import HTMLNode


# This class works with "Leaf Nodes" which are HTML nodes with no children
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    # This function will convert a "Leaf" Node into an HTML Node
    # If the value is empty throw an error, if the Tag is empty return the value alone
    def to_html(self):
        prop_list = []
        if self.value is None:
            raise ValueError("Value is required.")
        if self.tag is None:
            return self.value
        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        for prop in self.props:
            prop_list.append(f'{prop}="{self.props[prop]}"')
            full_str = " ".join(prop_list)
        return f'<{self.tag} {full_str}>{self.value}</{self.tag}>'
