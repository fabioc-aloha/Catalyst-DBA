# 🛠️ Scripts Folder

**Maintenance Responsibility**: Alex (AI Research Assistant) with Doctoral Candidate usage

**Purpose**: This folder contains automation scripts and tools that support your DBA research workflow, document processing, and system maintenance.

## 📄 Document Conversion Scripts

### 🔄 **Enhanced Document Converter** (Recommended)
**File**: `enhanced_document_converter.py`
- **Purpose**: Advanced PDF and DOCX to Markdown conversion
- **Features**: Table extraction, structure preservation, **in-place conversion**
- **Usage**: `python enhanced_document_converter.py input.pdf` (saves .md alongside original)
- **Best For**: Academic papers, handbooks, complex documents

### 🔄 **Basic Document Converter**
**File**: `document_converter.py`
- **Purpose**: Multi-format document conversion with academic focus
- **Features**: Citation handling, error recovery, **in-place conversion**
- **Usage**: `python document_converter.py input.pdf` (saves .md alongside original)
- **Best For**: Research papers, general academic documents### 📄 **PDF to Markdown Converter**
**File**: `pdf_to_markdown.py`
- **Purpose**: Simple PDF conversion with dual-library approach
- **Features**: Page-by-page extraction, clean formatting, **in-place conversion**
- **Usage**: `python pdf_to_markdown.py input.pdf` (saves .md alongside original)
- **Best For**: Quick conversions, simple PDF documents

### 📊 **PDF Table Enhancer**
**File**: `pdf_table_enhancer.py`
- **Purpose**: Post-processing for table formatting improvement
- **Features**: DBA handbook optimization, academic table enhancement
- **Usage**: `python pdf_table_enhancer.py converted_file.md`
- **Best For**: Enhancing tables after initial conversion

## 🧠 System Maintenance Scripts

### 🌙 **Neural Dream Protocol**
**File**: `neural-dream.ps1`
- **Purpose**: Automated system maintenance and optimization
- **Features**: Memory consolidation, synaptic maintenance, health monitoring
- **Usage**: `.\neural-dream.ps1`
- **Best For**: System optimization and cognitive architecture maintenance

## 📦 Setup and Installation

### Quick Setup:
```bash
# Install all dependencies (from root folder)
pip install -r ../requirements.txt

# Verify installation
python enhanced_document_converter.py --help
```

### Dependencies:
- **PDF Processing**: pdfplumber, PyPDF2, pymupdf
- **DOCX Processing**: python-docx, docx2txt
- **Table Enhancement**: pandas, tabulate
- **Optional**: beautifulsoup4, lxml

## 🎯 Usage for DBA Research

### Document Conversion Workflow:
1. **Convert** research documents to Markdown format **alongside originals** for AI analysis
2. **Enhance** table formatting for better readability (optional)
3. **Access** both original and converted formats in the same location
4. **Analyze** content with Alex's research assistance

### Recommended Use Cases:
- **Literature Review**: Convert journal articles (PDFs) alongside originals for easy reference
- **Academic Resources**: Convert DBA handbooks and university guidelines in-place
- **Research Materials**: Convert interview transcripts and survey results alongside originals
- **Committee Documents**: Convert feedback and requirement documents for dual access

### Example Workflow:
```bash
# Your research folder structure:
research/
├── handbooks/DBA_Guide.pdf
├── papers/literature_review.pdf
└── dissertations/chapter1.docx

# Convert documents in-place:
python scripts/enhanced_document_converter.py --batch research/

# Result - originals preserved, .md files added:
research/
├── handbooks/
│   ├── DBA_Guide.pdf    # Original
│   └── DBA_Guide.md     # AI-readable ✨
├── papers/
│   ├── literature_review.pdf  # Original
│   └── literature_review.md   # AI-readable ✨
└── dissertations/
    ├── chapter1.docx    # Original
    └── chapter1.md      # AI-readable ✨
```### Integration with Research Process:
- Use converted documents for literature analysis
- Enable Alex to read and analyze your research materials
- Support systematic literature review processes
- Facilitate content analysis and theoretical framework development

## 📚 Documentation

- **[Complete Setup Guide](DOCUMENT-CONVERSION-GUIDE.md)** - Detailed installation and usage instructions
- **[Requirements File](../requirements.txt)** - Python dependencies for easy installation

## 🔧 Troubleshooting

### Common Issues:
- **Import Errors**: Install missing dependencies with `pip install -r ../requirements.txt`
- **PDF Extraction Issues**: Try different scripts for different PDF types
- **Table Formatting**: Use the table enhancer for post-processing
- **Complex Documents**: May require manual review after conversion

### 🚫 Unsupported File Formats
**Currently supported**: PDF (`.pdf`), DOCX (`.docx`), DOC (`.doc`)

**If you get "❌ Unsupported file format" error:**

| Format | Solution |
|--------|----------|
| PowerPoint (`.ppt`, `.pptx`) | Export to Word handout → save as DOCX → convert |
| Excel (`.xls`, `.xlsx`) | Save as PDF → convert PDF |
| Images (`.jpg`, `.png`) | Use OCR to create searchable PDF → convert |
| Text files (`.txt`, `.rtf`) | Open in Word → save as DOCX → convert |
| Web pages (`.html`) | Print to PDF from browser → convert |
| E-books (`.epub`, `.mobi`) | Use Calibre to convert to PDF → convert |

**Quick conversion path**: `Your File → PDF/DOCX → Markdown`

📖 **[Full Format Guide](DOCUMENT-CONVERSION-GUIDE.md#🚫-handling-unreadable-file-formats)** - Complete solutions for all unsupported formats

### Getting Help:
Ask Alex: `"help with document conversion"` for guidance on:
- Script selection for your document type
- Troubleshooting conversion issues
- Optimizing output for research analysis
- Integration with your research workflow

This folder provides the tools needed to make your research documents accessible for AI analysis and support throughout your DBA journey.
