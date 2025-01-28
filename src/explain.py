from langchain_ollama import ChatOllama

llm = ChatOllama(model = "deepseek-r1",
                 temperature=0)

def get_desc(json_data, ask_about):
    messages = [
        (
            "system",
            """
            You are an analyst. Your goal is to answer the questions based on the most recent json data that will be provided to you.
            These are all in Philippine Peso and the data is from August 2024 to December 2024 only.
            """

        ),
        (
            "human",
            f"""
            Here is the data I want you to refer to: {json_data}
            
            State straightforward, brief description about {ask_about} expenses using the monthly data provided to you.
            """
        )
    ]

    return(llm.invoke(messages))