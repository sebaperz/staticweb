class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method must be implemented")

    def props_to_html(self) -> str:
        if self.props:
            return ''.join([f' {key}="{value}"' for key, value in self.props.items()])
        return ''

    def __repr__(self) -> str:
        return f"HtmlNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"

    def __eq__(self, other) -> bool:
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        if self.value is None and self.tag != "img":
            raise ValueError("All leaf nodes must have a value")

    def to_html(self) -> str:
        if self.tag == "img":  # this are 2 self line for image format
            return f"<{self.tag}{self.props_to_html()}>"
        if self.tag != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"{self.value}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have children")

    def to_html(self) -> str:
        if self.children is not None:
            return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
        raise ValueError("All parent nodes must have children")
