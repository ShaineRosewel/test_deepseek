from langchain_ollama import ChatOllama

llm = ChatOllama(model = "deepseek-r1",
                 temperature=0)

def get_desc(json_data, ask_about):
    messages = [
        (
            "system",
            """
            You are an analyst. Your goal is to provide insights and recommendations on how to save
            based on the most recent json data that will be provided to you. These are all in Philippine
            peso and the data is from August 2024 to December 2024 only. No need to repeat stating the numbers in words.
            """

        ),
        (
            "human",
            f"""
            Here is the data I want you to refer to: {json_data}
            
            State straightforward, brief insight & tips on saving about {ask_about} expenses using the monthly data provided to you.
            """
        )
    ]

    return(llm.invoke(messages))