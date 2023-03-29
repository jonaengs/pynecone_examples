"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import math
import pandas as pd
import numpy as np

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


# state_num0_val = 0
# state_num2_val = 2

# class State(pc.State):
#     """The app state."""
#     num0 = state_num0_val
#     num2 = state_num2_val
#     t = (1, 2)
#     # l = [1, math.nan]
#     l = data

# def generate_num0_statement(right_val):
#     eq_str = f"'{state_num0_val.__repr__()} == {right_val.__repr__()}'"
#     ineq_str = f"'{state_num0_val.__repr__()} != {right_val.__repr__()}'"
    
#     equality = pc.cond(
#         (State.num0 == right_val) == (state_num0_val == right_val), 
#         pc.text(eq_str + " Behaves the same way."), 
#         pc.text(eq_str + " Does not behave the same way.")
#     )
#     inequality = pc.cond(
#         (State.num0 != right_val) == (state_num0_val != right_val), 
#         pc.text(ineq_str + " Behaves the same way."), 
#         pc.text(ineq_str + " Does not behave the same way.")
#     )

#     return equality, inequality, pc.text("-"*20)

# def generate_num2_statement(right_val):
#     eq_str = f"'{state_num2_val.__repr__()} == {right_val.__repr__()}'"
#     ineq_str = f"'{state_num2_val.__repr__()} != {right_val.__repr__()}'"
    
#     equality = pc.cond(
#         (State.num2 == right_val) == (state_num2_val == right_val), 
#         pc.text(eq_str + " Behaves the same way."), 
#         pc.text(eq_str + " Does not behave the same way.")
#     )
#     inequality = pc.cond(
#         (State.num2 != right_val) == (state_num2_val != right_val), 
#         pc.text(ineq_str + " Behaves the same way."), 
#         pc.text(ineq_str + " Does not behave the same way.")
#     )

#     return equality, inequality, pc.text("-"*20)

# def index() -> pc.Component:
#     return pc.center(
#         pc.vstack(
#             pc.text(State.t),
#             pc.text(State.l),
#             pc.cond(State.l == math.nan, pc.text("asdasd")),

#             # pc.text(State.d),

#             # pc.text(State.s),
#         ),
#         # pc.vstack(
#         #     pc.text("Semantics", font_size="2em"),
#         #     *generate_num2_statement(2),
#         #     *generate_num2_statement(0),
#         #     *generate_num2_statement(True),
#         #     *generate_num2_statement(False),
#         #     *generate_num2_statement("2"),   
#         #     # *generate_num2_statement(None),

#         #     *generate_num0_statement(2),
#         #     *generate_num0_statement(0),
#         #     *generate_num0_statement(True),
#         #     *generate_num0_statement(False),
#         #     *generate_num0_statement("2"),   
#         #     # *generate_num0_statement(None),   
#         # ),
#         padding_top="10%",
#     )


# data = pd.DataFrame({
#     "name": ["jane", "rob", "harry"],
#     "age": [3, 2, 0],
#     "height_cm": [90, 80, 50],
#     # "annual_growth_cm": [30, 40, np.inf]  # height_cm / age. Division by 0 gives Infinity
# })
# data["annual_growth_cm"] = data["height_cm"] / data["age"]
# print(data)

class State(pc.State):
    nan = np.nan
    # nan = "nan"
    # data = data

def index() -> pc.Component:
    return pc.vstack(
        pc.text("asd")
        # pc.cond(State.nan, pc.text("a")),
        # pc.data_table(data=State.data)
        # pc.data_table(data=data)
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
