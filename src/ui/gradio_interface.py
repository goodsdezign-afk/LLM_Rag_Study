from src.config.config import CONFIG
import gradio as gr

def create_interface():
    print(CONFIG["openai_api_key"])


def launch_interface():
    demo = create_interface()
    