import pynecone as pc

config = pc.Config(
    app_name="mui_import",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=["react-copy-to-clipboard","@mui/material"],
)
