from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import json
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(model="gpt-4-turbo", openai_api_key=openai_api_key)

def process_document(text: str) -> dict:
    # Split large text
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    full_text = " ".join(chunks)  # For simplicity, combine; LangChain can handle chains

    # Translation prompt
    translate_prompt = PromptTemplate(
        input_variables=["text"],
        template="Translate this legal text into plain, easy-to-understand English: {text}"
    )
    translate_chain = LLMChain(llm=llm, prompt=translate_prompt)
    plain_translation = translate_chain.run(text=full_text)

    # Red flags prompt
    red_flags_prompt = PromptTemplate(
        input_variables=["text"],
        template="Identify predatory or risky clauses in this legal text. List them with reasons: {text}"
    )
    red_flags_chain = LLMChain(llm=llm, prompt=red_flags_prompt)
    red_flags_raw = red_flags_chain.run(text=full_text)
    red_flags = [{"clause": f.split(':')[0], "reason": f.split(':')[1]} for f in red_flags_raw.split('\n') if ':' in f]

    # Risk score (1-10 based on flags)
    risk_score = min(10, len(red_flags) * 2)  # Simple heuristic

    # Summary prompt
    summary_prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the key obligations in this legal document: {text}"
    )
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
    summary = summary_chain.run(text=full_text)

    # Clauses breakdown
    clauses_prompt = PromptTemplate(
        input_variables=["text"],
        template="Break down this legal text into clauses with titles and descriptions: {text}"
    )
    clauses_chain = LLMChain(llm=llm, prompt=clauses_prompt)
    clauses_raw = clauses_chain.run(text=full_text)
    clauses = [{"title": c.split(':')[0], "description": c.split(':')[1]} for c in clauses_raw.split('\n') if ':' in c]

    return {
        "plain_translation": plain_translation,
        "red_flags": red_flags,
        "risk_score": risk_score,
        "summary": summary,
        "clauses": clauses
    }

def answer_question(question: str, document_text: str) -> str:
    qa_prompt = PromptTemplate(
        input_variables=["question", "text"],
        template="Based on this legal document, answer the question: {question}. Document: {text}"
    )
    qa_chain = LLMChain(llm=llm, prompt=qa_prompt)
    return qa_chain.run(question=question, text=document_text)