# Adding LLM prompt
llm_prompt = """You are a knowledgeable assistant. Based on the provided context, provide precise to the point answer.
Do not repeat the same line of response if the answer is not known. Just mention that you do not know the answer.
Context: {context}
Question: {question}
Answer:
"""