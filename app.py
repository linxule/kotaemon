import os

from theflow.settings import settings as flowsettings

KH_APP_DATA_DIR = getattr(flowsettings, "KH_APP_DATA_DIR", ".")
GRADIO_TEMP_DIR = os.getenv("GRADIO_TEMP_DIR", None)
# override GRADIO_TEMP_DIR if it's not set
if GRADIO_TEMP_DIR is None:
    GRADIO_TEMP_DIR = os.path.join(KH_APP_DATA_DIR, "gradio_tmp")
    os.environ["GRADIO_TEMP_DIR"] = GRADIO_TEMP_DIR

# Get the PORT from environment variable for Railway
port = int(os.environ.get("PORT", 7860))

from ktem.main import App  # noqa

app = App()
demo = app.make()
demo.queue().launch(
    server_name="0.0.0.0",
    server_port=port,
    favicon_path=app._favicon,
    inbrowser=False,  # Changed to False for Railway deployment
    allowed_paths=[
        "libs/ktem/ktem/assets",
        GRADIO_TEMP_DIR,
    ],
)
