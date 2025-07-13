import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import time

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Test berbagai model
models = [
    "llama-3.3-70b-versatile",
    "deepseek-r1-distill-llama-70b", 
    "gemma2-9b-it"
]

temperatures = [0.1, 0.5, 0.9]

def test_model_response(model_name, temperature, prompt):
    """Test response dari model dengan parameter tertentu"""
    try:
        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=model_name,
            temperature=temperature
        )
        
        start_time = time.time()
        response = llm.invoke(prompt)
        end_time = time.time()
        
        return {
            "model": model_name,
            "temperature": temperature,
            "response": response.content,
            "response_time": end_time - start_time,
            "response_length": len(response.content)
        }
    except Exception as e:
        return {
            "model": model_name,
            "temperature": temperature,
            "error": str(e)
        }

# Test prompt untuk RAG
test_prompt = """Based on the following context, answer the question:

Context: Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed for every task.

Question: What is machine learning?"""

print("=== ANALISIS MODEL DAN TEMPERATURE ===\n")

# Test setiap model dengan temperature berbeda
for model in models:
    print(f"Model: {model}")
    print("-" * 50)
    
    for temp in temperatures:
        result = test_model_response(model, temp, test_prompt)
        
        if "error" not in result:
            print(f"Temperature: {temp}")
            print(f"Response Time: {result['response_time']:.2f}s")
            print(f"Response Length: {result['response_length']} chars")
            print(f"Response: {result['response'][:200]}...")
            print()
        else:
            print(f"Temperature: {temp} - Error: {result['error']}")
    
    print("=" * 70)
    print()
