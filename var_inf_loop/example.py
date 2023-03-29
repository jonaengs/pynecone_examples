import pynecone as pc

class MuiThemeProvider(pc.Component):
    library = "@mui/material/styles"
    tag = "ThemeProvider"

    theme = pc.Var()



class TextField(pc.Component):
    library = "@mui/material"
    tag = "TextField"

    id: str
    label: str
    variant: str

    @classmethod
    def get_triggers(cls):
        return super().get_triggers() | {"on_change"}


text_field = TextField.create
mui_theme_provider = MuiThemeProvider.create

class State(pc.State):
    """The app state."""

def index():
    """The main view."""
    return pc.box(
        mui_theme_provider(
            text_field(pc.input(),id='standard-basic', label='Standard', variant='standard')
        )
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()