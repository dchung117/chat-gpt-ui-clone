from dotenv import load_dotenv
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl
import config

load_dotenv()

@cl.on_chat_start
def main():
    prompt = PromptTemplate(
        template=config.TEMPLATE,
        input_variables = ["question"]
    )
    chain = LLMChain(
        prompt = prompt,
        llm = OpenAI(
            temperature=config.TEMPERATURE,
            streaming=True,
            verbose=True
        )
    )
    cl.user_session.set("llm_chain", chain)

@cl.on_message
async def message(msg: str) -> None:
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
    chain = cl.user_session.get("llm_chain")
    response = await chain.acall(
        msg,
        callbacks= [cl.AsyncLangchainCallbackHandler()]
    )
    await cl.Message(content=response["text"]).send()