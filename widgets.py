from pywebui.exceptions import InvalidHValueError, InvalidChildError
import os

stylesheets=[]

def reverse(array: list):
    return array[::-1]

class Root:
    def __init__(self, title="PyWebUI Website"):
        self.title = title
        self.children - {}
        self.children["title"] = []
        self.children["body"] = []
        self.tag = "html"

    def update_title(self, title):
        self.title = title

    def construct_html(self):
        

class Element:
    def __init__(self, parent, id, class_, type, text=None):
        self.parent = parent
        self.id = id
        self.class_ = class_
        self.text = text
        self.type = type
        self.children = []
        self.rendered = False

    def construct_html(self):
        element = f"<{self.type}"
        if self.alt:
            element += f' alt="{self.alt}"'
        if self.src:
            element += f' src="{self.src}"'
        if self.id:
            element += f' id="{self.id}"'
        if self.class_:
            element += f' class="{self.class_}"'
        element += ">"
        if self.text:
            element += self.text
        element += f"</{self.type}>"
        return element
    
    def add_child(self, child):
        if not issubclass(child.__class__, Element):
            raise InvalidChildError(f"Can not create a child with type {type(child)}. Child must derive from type type <class 'Element'>")
        self.children.append(child)


class StyleSheet:
    def __init__(self, widget: Element):
        self.widget = widget
        self.styles = {"default":{}, "hover":{}}

    def add_style(self, key: str, styles: str, type="default"):
        self.styles[type][key] = styles 
    
    def construct_stylesheet(self):
        if self.widget.id is not None:
            self.style = "#" + self.widget.id + "{\n"
        elif self.widget.class_:
            self.style = "." + self.widget.class_ + "{\n"
        curr_value = ""
        for key, value in self.styles["default"].items():
            self.style += f"\t {key}: {value};\n"
        self.style += "}"
        
        if bool(self.styles["hover"]):
            if self.widget.id is not None:
                self.style = "#" + self.widget.id + ":hover {\n"
            elif self.widget.class_:
                self.style = "." + self.widget.class_ + ":hover {\n"
            
            for key, value in self.styles["hover"].items():
                self.style += f"\t {key}: {value}; \n"
            self.style += "}"
        return self.style


class Image(Element):
    def __init__(self, parent, src: str, alt=None, id=None, class_=None):
        self.parent = parent
        self.id = id
        self.src = src
        self.alt = alt
        self.class_ = None
        self.type = "img"
        super().__init__(self.parent, self.id, self.class_, self.type)

class Container(Element):
    def __init__(self, parent, id, class_):
        self.parent = parent
        self.id = id,
        self.class_ = class_
        self.tag = "div"

class Header(Element):
    def __init__(self, parent, id, class_, text=None, h_num=1):
        if h_num > 6: raise InvalidHValueError(f"h_value can not be greater than 6. <h1 : h2: h3: h4: h5: h6>")
        self.type = f"h{h_num}"
        self.id = id
        self.h_num = h_num
        self.class_ = class_
        self.tag = f"h{self.h_num}"
        self.text = text


def run(main: Root):
    pass

