from dotenv import load_dotenv
import chainlit as cl
import openai

load_dotenv()

@cl.on_message
async def main(msg: str):
    await cl.Message(content=msg).send()