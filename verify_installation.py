#!/usr/bin/env python3
"""
Installation verification script for RAG_with_GroqAPI

This script checks if all required dependencies are installed correctly
and verifies that CPU-only PyTorch is being used (no CUDA dependencies).
"""

import sys

def check_import(module_name, import_statement, description):
    """Check if a module can be imported successfully."""
    try:
        exec(import_statement)
        print(f"✓ {description}")
        return True
    except ImportError as e:
        print(f"✗ {description} - Error: {e}")
        return False
    except Exception as e:
        print(f"⚠ {description} - Warning: {e}")
        return True

def main():
    print("=" * 60)
    print("RAG with GroqAPI - Installation Verification")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Core dependencies
    print("Checking core dependencies...")
    checks = [
        ("langchain", "import langchain", "LangChain"),
        ("langchain_community", "from langchain_community.document_loaders import PyPDFLoader", "LangChain Community"),
        ("langchain_groq", "from langchain_groq import ChatGroq", "LangChain Groq"),
        ("gradio", "import gradio", "Gradio UI"),
        ("pypdf", "import pypdf", "PyPDF"),
        ("dotenv", "from dotenv import load_dotenv", "Python-dotenv"),
        ("faiss", "import faiss", "FAISS-CPU"),
        ("groq", "import groq", "Groq API client"),
    ]
    
    for module, import_stmt, desc in checks:
        if not check_import(module, import_stmt, desc):
            all_good = False
    
    print()
    
    # PyTorch verification
    print("Checking PyTorch installation...")
    try:
        import torch
        version = torch.__version__
        cuda_available = torch.cuda.is_available()
        
        print(f"✓ PyTorch version: {version}")
        
        if '+cpu' in version:
            print("✓ CPU-only PyTorch detected (recommended)")
        elif not cuda_available:
            print("✓ PyTorch without CUDA support (good for deployment)")
        else:
            print("⚠ PyTorch with CUDA support detected (may cause deployment issues)")
            
        print(f"  CUDA available: {cuda_available}")
        
    except ImportError:
        print("✗ PyTorch not installed")
        all_good = False
    
    print()
    
    # Sentence transformers verification
    print("Checking sentence-transformers...")
    try:
        import sentence_transformers
        print(f"✓ Sentence-transformers version: {sentence_transformers.__version__}")
    except ImportError:
        print("✗ Sentence-transformers not installed")
        all_good = False
    
    print()
    
    # Environment variables check
    print("Checking environment setup...")
    import os
    if os.path.exists('.env'):
        print("✓ .env file found")
    else:
        print("⚠ .env file not found (create from .env.example)")
    
    groq_key = os.environ.get("GROQ_API_KEY")
    if groq_key:
        print("✓ GROQ_API_KEY environment variable set")
    else:
        print("⚠ GROQ_API_KEY not set (required for operation)")
    
    print()
    print("=" * 60)
    
    if all_good:
        print("🎉 Installation verification PASSED!")
        print("Your RAG application should work correctly.")
    else:
        print("❌ Installation verification FAILED!")
        print("Please check the errors above and reinstall missing packages.")
        sys.exit(1)
    
    print()
    print("To run the application:")
    print("  python app.py")
    print()

if __name__ == "__main__":
    main()