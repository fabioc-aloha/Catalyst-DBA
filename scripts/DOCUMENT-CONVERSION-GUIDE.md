# Document Conversion Scripts - Setup & Usage Guide

🔄 **Research Document Conversion Suite** - Convert PDF and DOCX files to Markdown format for AI analysis

## 📦 Installation Requirements

### Python Dependencies

Install the required Python packages using pip:

```bash
# Core PDF processing libraries
pip install pdfplumber PyPDF2 pymupdf

# DOCX processing libraries
pip install python-docx docx2txt

# Optional: Enhanced table processing
pip install pandas tabulate

# For enhanced formatting (if using advanced features)
pip install beautifulsoup4 lxml
```

### Quick Install (All Dependencies)

```bash
pip install pdfplumber PyPDF2 pymupdf python-docx docx2txt pandas tabulate beautifulsoup4 lxml
```

## 🛠️ Available Scripts

### 1. **Enhanced Document Converter** (Recommended)
**File**: `enhanced_document_converter.py`
**Features**:
- Advanced PDF and DOCX conversion
- Table extraction and formatting
- Structure preservation
- Batch processing
- 1100+ lines of comprehensive functionality

**Usage**:
```bash
# Convert single file (saves .md in same directory)
python enhanced_document_converter.py input.pdf

# Batch convert directory (saves .md files alongside originals)
python enhanced_document_converter.py --batch ./documents/

# Optional: Custom output directory
python enhanced_document_converter.py input.pdf --output ./converted/

# Verbose logging
python enhanced_document_converter.py input.pdf --verbose
```

### 2. **Basic Document Converter**
**File**: `document_converter.py`
**Features**:
- Multi-format support
- Academic citation handling
- Error recovery
- **In-place conversion** (saves .md alongside original)
- Batch processing

**Usage**:
```bash
# Convert single file (saves .md in same directory)
python document_converter.py input.pdf

# Batch convert (saves .md files alongside originals)
python document_converter.py --batch ./docs/

# Optional: Custom output directory
python document_converter.py --batch ./docs/ --output ./markdown/
```

### 3. **PDF to Markdown (Simple)**
**File**: `pdf_to_markdown.py`
**Features**:
- Simple PDF conversion
- Dual-library approach (PyPDF2 + pdfplumber)
- Page-by-page extraction
- **In-place conversion** (saves .md alongside original)

**Usage**:
```bash
# Convert PDF (saves .md in same directory)
python pdf_to_markdown.py input.pdf
```

### 4. **PDF Table Enhancer**
**File**: `pdf_table_enhancer.py`
**Features**:
- Post-processing for table formatting
- DBA handbook optimization
- Academic document table enhancement

**Usage**:
```bash
# Enhance tables in converted markdown
python pdf_table_enhancer.py converted_file.md

# Process entire directory
python pdf_table_enhancer.py ./converted_docs/
```

## 🔄 Recommended Workflow (In-Place Conversion)

### **Default Behavior: Files Saved Alongside Originals**

By default, all conversion scripts save the `.md` files in the same directory as the source documents. This approach provides several benefits:

- **Easy Management**: Converted files stay with their originals
- **Clear Organization**: No need to track separate output folders
- **Version Control**: Easy to see which documents have been converted
- **Quick Access**: Both formats available in the same location

### **Example Directory Structure After Conversion**:
```
research_docs/
├── handbooks/
│   ├── DBA_Handbook.pdf          # Original PDF
│   ├── DBA_Handbook.md           # Converted Markdown ✨
│   ├── Student_Guide.docx        # Original DOCX
│   └── Student_Guide.md          # Converted Markdown ✨
├── papers/
│   ├── Literature_Review.pdf     # Original PDF
│   ├── Literature_Review.md      # Converted Markdown ✨
│   ├── Research_Paper.docx       # Original DOCX
│   └── Research_Paper.md         # Converted Markdown ✨
└── scripts/                      # Conversion scripts
```

### **For Single Documents:**
```bash
# Convert PDF to .md in same directory
python scripts/enhanced_document_converter.py handbooks/DBA_Handbook.pdf
# Result: handbooks/DBA_Handbook.md created

# Convert DOCX to .md in same directory
python scripts/enhanced_document_converter.py papers/Research_Paper.docx
# Result: papers/Research_Paper.md created
```

### **For Batch Processing:**
```bash
# Convert all PDFs and DOCX files in a directory
python scripts/enhanced_document_converter.py --batch handbooks/
# Result: .md files created alongside each original

# Convert all files in multiple directories
python scripts/enhanced_document_converter.py --batch papers/
python scripts/enhanced_document_converter.py --batch dissertations/
```

### **Optional: Custom Output Directory**
If you prefer a separate output directory, you can still specify one:
```bash
# Convert to separate directory (alternative approach)
python scripts/enhanced_document_converter.py handbooks/DBA_Handbook.pdf --output ./converted/
```

## 📁 Suggested Directory Structure

```
research_docs/
├── original/              # Original PDF/DOCX files
│   ├── handbooks/
│   ├── papers/
│   └── dissertations/
├── converted/             # Markdown output
│   ├── handbooks/
│   ├── papers/
│   └── dissertations/
└── scripts/               # Conversion scripts (this folder)
    ├── enhanced_document_converter.py
    ├── document_converter.py
    ├── pdf_to_markdown.py
    └── pdf_table_enhancer.py
```

## ⚡ Quick Start Examples

### Convert DBA Handbook (In-Place):
```bash
# Convert DBA handbook - saves .md alongside original PDF
python enhanced_document_converter.py "handbooks/DBA_Handbook.pdf"
# Result: handbooks/DBA_Handbook.md created

# Enhance table formatting
python pdf_table_enhancer.py "handbooks/DBA_Handbook.md"
```

### Convert Research Papers (Batch):
```bash
# Convert all papers - saves .md files alongside originals
python enhanced_document_converter.py --batch ./papers/
# Result: Each .pdf/.docx gets a corresponding .md file
```

### Convert Dissertation Chapters:
```bash
# Convert DOCX chapter - saves .md alongside original
python enhanced_document_converter.py "dissertation/Chapter1_Introduction.docx"
# Result: dissertation/Chapter1_Introduction.md created
```

### Real-World Example:
```bash
# Your research folder before conversion:
research/
├── handbook.pdf
├── paper1.pdf
└── dissertation_draft.docx

# Run batch conversion:
python scripts/enhanced_document_converter.py --batch research/

# Your research folder after conversion:
research/
├── handbook.pdf
├── handbook.md          ✨ New!
├── paper1.pdf
├── paper1.md            ✨ New!
├── dissertation_draft.docx
└── dissertation_draft.md ✨ New!
```

## 🎯 Integration with DBA Research

### Research Literature Conversion:
- Convert PDF journals articles for analysis
- Extract tables and figures from academic papers
- Process conference proceedings for literature review

### Academic Document Processing:
- Convert DBA handbook sections for reference
- Process university guidelines and requirements
- Convert committee feedback documents

### Data Analysis Preparation:
- Convert survey results and reports
- Process interview transcripts (if in document format)
- Convert organizational documents for case studies

## 🔧 Troubleshooting

### Common Issues:

**PDF Extraction Errors**:
- Try different PDF libraries (script includes fallbacks)
- Check if PDF is scanned image (may need OCR)
- Verify file isn't password protected

**DOCX Processing Issues**:
- Ensure file isn't corrupted
- Check for complex formatting that may need manual review
- Try opening in Word first to verify accessibility

**Table Formatting Problems**:
- Use the table enhancer script for post-processing
- Complex tables may need manual adjustment
- Consider using the enhanced converter for better table detection

### Getting Help:
Ask Alex: `"help with document conversion"` for specific guidance on:
- Script selection for your document type
- Troubleshooting conversion issues
- Optimizing output for research analysis
- Batch processing strategies

## 🚫 Handling Unreadable File Formats

### Currently Supported Formats
The conversion scripts support these document formats:
- ✅ **PDF files** (`.pdf`) - Academic papers, handbooks, reports
- ✅ **DOCX files** (`.docx`) - Modern Word documents
- ✅ **DOC files** (`.doc`) - Legacy Word documents

### Unsupported Format Error
If you encounter this error:
```
❌ Unsupported file format: .xyz
```

**The script has detected a file type that cannot be processed.** Here's what to do:

### 🔄 Solutions for Common Unreadable Formats

#### **PowerPoint Files (`.ppt`, `.pptx`)**
```bash
# Manual conversion needed:
# 1. Open in PowerPoint
# 2. File → Export → Create Handouts → Send to Microsoft Word
# 3. Save as .docx, then convert:
python enhanced_document_converter.py presentation_handout.docx
```

#### **Excel Files (`.xls`, `.xlsx`)**
```bash
# For tabular data extraction:
# 1. Open in Excel
# 2. Save As → PDF (preserve formatting)
# 3. Convert the PDF:
python enhanced_document_converter.py spreadsheet_data.pdf
```

#### **Image Files (`.jpg`, `.png`, `.tiff`)**
```bash
# OCR conversion required:
# 1. Use online OCR tool (Google Docs, Adobe Acrobat)
# 2. Convert image to searchable PDF
# 3. Then convert:
python enhanced_document_converter.py scanned_document.pdf
```

#### **Text Files (`.txt`, `.rtf`)**
```bash
# Simple text files:
# 1. Open in Word
# 2. Save As → .docx format
# 3. Convert:
python enhanced_document_converter.py text_document.docx

# Alternative: Manual conversion
# Text files are already readable - copy content to markdown manually
```

#### **Web Pages (`.html`, `.htm`)**
```bash
# For web content:
# 1. Print to PDF from browser (Ctrl+P → Save as PDF)
# 2. Convert the PDF:
python enhanced_document_converter.py webpage_content.pdf
```

#### **E-books (`.epub`, `.mobi`)**
```bash
# E-book conversion:
# 1. Use Calibre (free software) to convert to PDF
# 2. Then convert:
python enhanced_document_converter.py ebook_content.pdf
```

#### **Protected or Encrypted Files**
```bash
# For password-protected documents:
# 1. Open with correct password
# 2. Save As → unprotected version
# 3. Convert the unprotected file

# For DRM-protected content:
# Research ethical and legal conversion options
```

### 🛠️ General Troubleshooting for Unreadable Files

#### **Step 1: Check File Extension**
```bash
# Verify the actual file type:
file your_document.xyz  # On Linux/Mac
# Or check Properties in Windows

# Sometimes files have wrong extensions
```

#### **Step 2: Try Alternative Viewers**
- **Adobe Acrobat Reader** - For complex PDFs
- **LibreOffice** - For various document formats
- **Google Docs** - Upload and convert online
- **OneDrive/Office 365** - Online conversion tools

#### **Step 3: Convert to Supported Format**
```bash
# Universal conversion path:
Your File → PDF → Markdown

# Or:
Your File → DOCX → Markdown
```

#### **Step 4: Request Help from Alex**
If file conversion is challenging, ask for specific guidance:

```
Alex, I have a [file type] document about [topic] that I need to convert for analysis.
What's the best approach for [specific file format]?
```

### 📋 Pre-Conversion Checklist

Before attempting conversion, verify:
- [ ] File is not corrupted (opens in native application)
- [ ] File is not password-protected
- [ ] File extension matches actual format
- [ ] File contains text content (not just images)
- [ ] You have appropriate software to view the file
- [ ] File size is reasonable (< 100MB for best results)

### 🔍 Format Detection Tips

**Unknown file types:**
```bash
# Check file headers (first few bytes)
hexdump -C -n 16 unknown_file.xyz

# Common signatures:
# PDF: %PDF
# DOCX: PK (ZIP archive)
# DOC: Microsoft Office Document
```

### 💡 Best Practices for Research Documents

1. **Standardize on Supported Formats**:
   - Request PDFs for research papers
   - Use DOCX for collaborative documents

2. **Convert at Source**:
   - Ask document providers for PDF/DOCX versions
   - Convert immediately when receiving unsupported formats

3. **Maintain Original Files**:
   - Keep original format alongside converted versions
   - Document conversion method for reproducibility

4. **Quality Check After Conversion**:
   - Review markdown output for completeness
   - Check table formatting and structure
   - Verify academic citations are preserved

### 🚨 When Conversion Isn't Possible

Some files cannot be meaningfully converted:
- **Pure image files** without OCR
- **Heavily encrypted documents**
- **Proprietary formats** without viewers
- **Corrupt or damaged files**

In these cases:
1. **Document the limitation** in your research notes
2. **Seek alternative sources** for the same information
3. **Consider manual transcription** for critical content
4. **Ask Alex for alternative analysis approaches**

This conversion suite enables you to make your research documents accessible to me for analysis, literature review support, and research guidance throughout your DBA journey!
