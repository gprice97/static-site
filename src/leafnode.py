class LeafNode:
    def __init__(self, value, tag, props=None):
        super().__init__(tag=tag)
        self.value = value
        self.props = props if props is None else {}

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required.")
        if self.tag is None:
            return self.value
        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'

        return f'<{self.tag} {self.props}>{self.value}</{self.tag}>'
