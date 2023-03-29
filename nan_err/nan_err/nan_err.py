import pynecone as pc
import ast
import re

def to_template_literal(s: str) -> str:
    """
    Takes a formatted Python f-string with references to Pynecone Vars
    and turns it into a fully functional Javascript template literal
    with working references to those same state variables.

    Most of the heavy lifting has already been done by the 
    Var class, transforming the Python code inside the f-string's 
    format blocks into valid and equivalent (ish) Javascript.

    Because Python's f-string syntax and Javascript's template literal
    syntax are so similar, all we have to do is add the $ in front 
    of the bits we want to be formatted.
    """
    def process(expr: ast.expr):
        if isinstance(expr, ast.Constant):
            return expr.value
        elif isinstance(expr, ast.FormattedValue):
            return "$" + ast.unparse(expr)
        raise ValueError()  # Not sure if arriving here is actually possible. Just here for safety

    # Turn the string into an f-string and parse it with the built-in ast,
    # simply adding 
    f_str = 'f"' + s.replace('"', "'") + '"'
    f_str_ast = ast.parse(f_str, mode="eval")
    str_parts = f_str_ast.body.values

    # We don't need to surround with '`' because pc already does this
    # with all strings that get compiled to JS.
    out = "".join(map(process, str_parts))
    return out

def to_template_literal(s: str) -> str:
    s = re.sub(r"([^{]){([^{])", r"\1${\2", s)
    return s

class SubState(pc.State):
    strs: list[str] = ["test"]

class State(pc.State):
    colors: dict[str, str] = {"one": "red", "two": "blue"}
    array: list[SubState] = [SubState()]
    color_key = "one"

    def toggle_color(self):
        self.color_key = "two" if self.color_key == "one" else "one"


def index():
    s = f'{1} and {State.color_key} and {State.colors[State.color_key]} and {State.array[0].strs[0]}'
    s_templated = to_template_literal(s)
    return pc.vstack(
        pc.text(s, color=State.colors[State.color_key]),
        pc.text(s_templated, color=State.colors[State.color_key]),
        pc.button("Toggle color", on_click=State.toggle_color)
    )


app = pc.App(state=State)
app.add_page(index)
app.compile()
