from langchain_ollama import ChatOllama

llm = ChatOllama(model = "deepseek-r1",
                 temperature=0)

def get_desc(json_data, ask_about):
    messages = [
        (
            "system",
            """
            You are an analyst. Your goal is to describe the trend, or if none, highlight a value that stands out.  
            You will be given monthly expense/spend data in Philippine pesos from August 2024 to December 2024 for a specific category.  

            Instructions:  
            - Provide a **straightforward and brief** insight into the trend.  
            - If no trend is clear, mention the most notable value.  
            - Include a **practical tip** for saving on {ask_about} expenses.  
            - **Do not** repeat numbers in words.  
            - Keep your response **concise and to the point**.
            """

        ),
        (
            "human",
            f"""
            Here is the data I want you to refer to: {json_data}  

            State a straightforward, brief insight & a tip on saving money related to {ask_about} expenses using the monthly data provided.
            """
        )
    ]

    return(llm.invoke(messages))