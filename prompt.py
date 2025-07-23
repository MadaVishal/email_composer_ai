from langchain import PromptTemplate

def get_email_prompt():
    template = """
    You are an expert email writer. Write a {tone} email for the following purpose:

    Purpose : {purpose}
    Additional Info : {details}

    The email should be professional, clear, and appropriate for the given tone.
    """

    return PromptTemplate.from_template(template)