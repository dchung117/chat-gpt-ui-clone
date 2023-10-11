from dotenv import load_dotenv
import chainlit as cl
import openai

MODEL = "gpt-4"
SYSTEM_PROMPT = "You are a helpful assistant."
TEMPERATURE = 1
load_dotenv()

@cl.on_message
async def main(msg: str) -> None:
    """
    Send Chat-GPT response back to user based on message.

    Args
    ----
        msg: str
            User message to chatbot.

    Return
    ------
        None
    """
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages = [
            {"role": "assistant", "content": SYSTEM_PROMPT},
            {"role": "user", "content": msg}
        ],
        temperature=TEMPERATURE,
    )
    await cl.Message(content=response["choices"][0]["message"]["content"]).send()