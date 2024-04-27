""" create and return propmt template """

from langchain.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)


def get_chat_prompt_template():
    """generate and return the prompt
    template that will answer the users query
    """
    return ChatPromptTemplate(
        input_variables=["content", "messages"],
        messages=[
            SystemMessagePromptTemplate.from_template(
                """
                    You are a helpful ai assistent.
                    try to answer the questions to the best of your knowledge
                """
            ),
            MessagesPlaceholder(variable_name="messages"),
            HumanMessagePromptTemplate.from_template("{content}"),
        ],
    )
