# app/rag/pipeline.py
def run_rag(question):
    chunks = retriever.search(question)
    context = "\n".join(chunks)
    prompt = render_prompt("qa.jinja", context=context, question=question)
    return llm.chat([{"role": "user", "content": prompt}])
