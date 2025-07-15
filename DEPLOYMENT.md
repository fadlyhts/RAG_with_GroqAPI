# Deployment Guide

## CPU-Only Installation (for Cloud Platforms like EasyPanel)

This application has been optimized for CPU-only deployments to avoid downloading large CUDA packages that cause deployment timeouts.

### Quick Start

1. **Standard Installation** (recommended for cloud deployments):
```bash
pip install -r requirements.txt
```

The requirements.txt file includes `--extra-index-url https://download.pytorch.org/whl/cpu` which ensures PyTorch and related packages install CPU-only versions.

2. **Alternative Installation** (if the extra-index-url doesn't work):
```bash
pip install --index-url https://download.pytorch.org/whl/cpu torch>=2.0.0
pip install -r requirements.txt --no-deps torch torchvision torchaudio
pip install -r requirements.txt
```

### Benefits of CPU-Only Installation

- **Faster deployments**: Avoids downloading 571MB+ CUDA packages
- **More reliable**: Prevents connection timeouts during package installation  
- **Smaller container size**: Reduces the overall application footprint
- **Cloud compatible**: Works on platforms without GPU access

### Verification

After installation, verify CPU-only mode:
```python
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")  # Should be False
```

Expected output:
```
PyTorch version: 2.x.x+cpu
CUDA available: False
```

The application will work identically with CPU-only PyTorch, just without GPU acceleration (which isn't needed for most RAG applications).