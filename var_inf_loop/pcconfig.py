import pynecone as pc

config = pc.Config(
    app_name="var_inf_loop",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
