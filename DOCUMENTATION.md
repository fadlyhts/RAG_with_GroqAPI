# RAG with Groq API - Complete Documentation

## Deskripsi Project

Project ini adalah implementasi sistem Retrieval-Augmented Generation (RAG) yang menggunakan Groq API untuk memberikan respons yang akurat berdasarkan dokumen PDF yang diunggah. Sistem ini menggabungkan kemampuan pencarian dokumen dengan kekuatan Large Language Model untuk memberikan jawaban yang kontekstual.

## Arsitektur Sistem

```
PDF Upload → Document Processing → Text Chunking → Embedding Generation → Vector Storage (FAISS)
                                                                                    ↓
User Question → Similarity Search → Context Retrieval → LLM Processing → Response
```

## Komponen Teknologi

1. **LangChain**: Framework untuk membangun aplikasi dengan LLM
2. **Groq API**: Platform AI yang menyediakan akses ke berbagai model LLM
3. **FAISS**: Vector database untuk pencarian similarity yang efisien
4. **HuggingFace Embeddings**: Model untuk mengkonversi teks menjadi representasi vektor
5. **Gradio**: Framework untuk membuat interface web yang interaktif
6. **PyPDF**: Library untuk memproses file PDF

## Fitur Utama

- Upload dan proses file PDF
- Pemecahan dokumen menjadi chunk-chunk yang optimal
- Pencarian konteks yang relevan menggunakan similarity search
- Integrasi dengan multiple LLM models (Llama, Deepseek, Gemma)
- Interface web yang user-friendly
- Support untuk berbagai konfigurasi temperature

## Model Yang Didukung

1. **llama-3.3-70b-versatile**: Model yang cepat dan konsisten
2. **deepseek-r1-distill-llama-70b**: Model dengan reasoning process yang detail
3. **gemma2-9b-it**: Model yang efisien untuk respons singkat

## Konfigurasi Temperature

- **Low (0.1-0.3)**: Respons yang konsisten dan fokus
- **Medium (0.4-0.6)**: Keseimbangan antara kreativitas dan konsistensi
- **High (0.7-0.9)**: Respons yang kreatif dan bervariasi

## Troubleshooting

### Error: GROQ_API_KEY tidak ditemukan
- Pastikan file `.env` sudah dibuat dan berisi API key yang valid
- Periksa format API key di file `.env`

### Error saat install dependencies
- Pastikan Python versi 3.8+ terinstall
- Gunakan virtual environment untuk menghindari konflik dependencies
- Jalankan `python verify_installation.py` untuk memverifikasi instalasi

### Error: Connection timeout saat install PyTorch/CUDA
- Project ini sudah dikonfigurasi untuk menggunakan CPU-only PyTorch
- Jika masih ada masalah, lihat `DEPLOYMENT.md` untuk panduan instalasi khusus cloud platform
- Untuk cloud deployment (EasyPanel, Heroku, dll), gunakan CPU-only installation

### Aplikasi tidak bisa diakses
- Periksa apakah port 7860 tidak digunakan aplikasi lain
- Coba restart aplikasi atau ganti port di kode

## Kontribusi

1. Fork repository ini
2. Buat branch untuk fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## Lisensi

Project ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail lengkap.

## Kontak

Jika ada pertanyaan atau saran, silakan buat issue di repository ini atau hubungi pengembang melalui email.
