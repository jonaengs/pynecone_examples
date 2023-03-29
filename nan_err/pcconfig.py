import pynecone as pc

config = pc.Config(
    app_name="nan_err",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
