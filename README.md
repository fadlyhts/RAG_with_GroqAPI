<h1 align="center"> Retrieval-Augmented Generation with Gradio and Groq API Key</h1>
<p align="center"> Natural Language Processing Project</p>

<div align="center">

<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">

</div>

### Name : Ahmad Fadli Hutasuhut
### Tech Stack : Python, Gradio, LangChain, HuggingFace Embedding, FAISS vector store

---

### 1. Analysis about how the project works

Proyek ini mengimplementasikan sistem Retrieval-Augmented Generation (RAG) yang menggunakan beberapa komponen utama:

1. **Document Processing**: Menggunakan PyPDFLoader untuk memuat dan memproses file PDF, kemudian membaginya menjadi chunk-chunk kecil menggunakan CharacterTextSplitter.

2. **Embedding & Vector Store**: Menggunakan HuggingFaceEmbeddings dengan model "sentence-transformers/all-MiniLM-L6-v2" untuk mengkonversi teks menjadi vektor, dan FAISS sebagai vector database untuk penyimpanan dan pencarian similarity.

3. **LLM Integration**: Mengintegrasikan dengan Groq API menggunakan ChatGroq untuk mendapatkan respons dari large language model.

4. **Retrieval Chain**: Menggunakan RetrievalQA chain dari LangChain yang menggabungkan retrieval system dengan LLM untuk memberikan jawaban berdasarkan konteks yang relevan.

5. **User Interface**: Menggunakan Gradio untuk membuat interface web yang user-friendly dengan fitur upload PDF dan chat interface.

Alur kerja: User upload PDF → Document chunking → Embedding generation → Vector storage → User bertanya → Similarity search → Context retrieval → LLM processing → Answer generation

### 2. Analysis about how different every model works on Retrieval-Augmented Generation

```python
def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile", # Change the model in the code
        temperature=0.2
    )
```
- Model used : `[llama-3.3-70b-versatile, deepseek-r1-distill-llama-70b, gemma2-9b-it]`

2.1 Analysis on `llama-3.3-70b-versatile`:

- **Performance**: Memberikan respons yang konsisten dan cepat (rata-rata 1-1.4 detik)
- **Response Quality**: Jawaban yang diberikan akurat dan sesuai dengan konteks, tidak mengulang informasi yang sudah ada di prompt
- **Temperature Behavior**: Tidak terpengaruh signifikan oleh perubahan temperature, menunjukkan stabilitas yang baik
- **Use Case**: Ideal untuk aplikasi yang membutuhkan konsistensi dan kecepatan respons

2.2 Analysis on `deepseek-r1-distill-llama-70b`:

- **Performance**: Waktu respons lebih lambat (2-6 detik) dengan variasi besar tergantung temperature
- **Response Quality**: Memiliki fitur "thinking process" yang menampilkan proses reasoning model, memberikan jawaban yang lebih detailed
- **Temperature Behavior**: Sangat sensitif terhadap temperature - pada temperature tinggi (0.9) menghasilkan respons yang sangat panjang dengan proses berpikir yang kompleks
- **Use Case**: Cocok untuk aplikasi yang membutuhkan transparansi dalam proses reasoning dan analisis mendalam

2.3 Analysis on `gemma2-9b-it`:

- **Performance**: Respons yang stabil dengan waktu pemrosesan menengah (1-2 detik)
- **Response Quality**: Memberikan jawaban yang ringkas dan to-the-point, reformulasi informasi dengan baik
- **Temperature Behavior**: Relatif stabil terhadap perubahan temperature, konsisten dalam kualitas output
- **Use Case**: Baik untuk aplikasi yang membutuhkan jawaban singkat dan langsung

### 3. Analysis about how temperature works

```python
def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile",
        temperature=0.2 # Change the temperature value here and analzye
    )
```

3.1 Analysis on higher temperature (0.9):

- **Creativity & Variability**: Temperature tinggi menghasilkan respons yang lebih kreatif dan bervariasi
- **deepseek-r1-distill-llama-70b**: Pada temperature 0.9, model ini menghasilkan proses reasoning yang sangat panjang dan kompleks (3400+ characters) dengan waktu pemrosesan yang lama (6+ detik)
- **Response Length**: Cenderung menghasilkan jawaban yang lebih panjang dan elaborate
- **Consistency**: Kurang konsisten dalam format dan panjang respons
- **Use Case**: Baik untuk brainstorming, creative writing, atau ketika membutuhkan perspektif yang beragam

3.2 Analysis on lower temperature (0.1):

- **Consistency**: Menghasilkan respons yang sangat konsisten dan predictable
- **Fokus**: Jawaban lebih fokus dan to-the-point tanpa tambahan informasi yang tidak perlu
- **Speed**: Umumnya lebih cepat dalam pemrosesan
- **Accuracy**: Lebih akurat dalam mengikuti instruksi dan konteks yang diberikan
- **Use Case**: Ideal untuk aplikasi production yang membutuhkan hasil yang dapat diprediksi dan konsisten

### 4. How to run the project

- Clone this repository with:

```git
git clone https://github.com/faldyhts/RAG_with_GroqAPI.git
```

- Copy the `.env.example` file and rename it to `.env`

```bash
GROQ_API_KEY=your-groq-api-key
```

- Fill the `GROQ_API_KEY` with your Groq API Key, find it here: <https://console.groq.com/keys>

- Navigate to the project directory:

```bash
cd RAG_with_GroqAPI
```

- Create a virtual environment:

```bash
python -m venv venv
```

- Activate the virtual environment:

**For Windows:**

```bash
.\venv\Scripts\Activate.ps1
```

**For Linux/Mac:**

```bash
source venv/bin/activate
```

- Install all required dependencies:

```bash
pip install -r requirements.txt
```

**Note:** The application uses CPU-only versions of PyTorch to avoid large CUDA package downloads, making deployments faster and more reliable on cloud platforms like EasyPanel. See `DEPLOYMENT.md` for more details.

- Verify the installation:

```bash
python verify_installation.py
```

- Run the application:

```bash
python app.py
```

- Open your web browser and navigate to the URL shown in the terminal (typically `http://127.0.0.1:7860`)

- Upload a PDF file and start asking questions about the document content!
