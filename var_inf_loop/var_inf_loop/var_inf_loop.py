import pynecone as pc
import sys
from itertools import chain

class Comp(pc.Component):
    tag = "a"
    a = pc.Var()


def create_nested(nesting = 0):
    chars = [f"A{i}" for i in range(100)]
    prev = None

    # Deeply nested
    for c_name in chars:
        prev = type(c_name, (pc.State, ), {"prev": (prev if prev is None else prev(), pc.State)})

    # Wide 
    # fields = {
    #     c_name: (type(c_name, (pc.State, ), {}), pc.State)
    #     for c_name in chars
    # }
    # prev = type("Top", (pc.State, ), fields)
    
    print(prev)
    return prev()

class S(pc.State):
    v: pc.State = create_nested()


def index() -> pc.Component:
    # create_nested()
    # return pc.cond(S.v, pc.text("hello"))
    return Comp.create(pc.text())


sys.setrecursionlimit(400)
app = pc.App(state=S)
app.add_page(index)
app.compile()