""" chat app with ollama llama3 model """

from llm import get_llm
from prompt import get_chat_prompt_template
from chain import create_chain
from dotenv import load_dotenv

""" load the env variables """
load_dotenv()


""" LARGE LANGUAGE MODEL """
llm = get_llm()

""" PROMPT """
prompt = get_chat_prompt_template()

""" CHAIN """
chain = create_chain(llm, prompt)


""" RUN THE APP """
if __name__ == "__main__":
    while True:
        qus = input(">>> ")
        """ user types q break out of the loop """
        if qus == "q":
            break
        """ print out the response from the model """
        for res in chain.stream({"content": qus}):
            print(res, end="", flush=True)
