#!/usr/bin/env python3
"""
PDF to Markdown Converter for DBA Handbook Analysis
Converts PDF files to markdown format for easier text analysis and comparison
"""

import PyPDF2
import pdfplumber
import re
import sys
from pathlib import Path

def extract_text_pypdf2(pdf_path):
    """Extract text using PyPDF2"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                if page_text.strip():
                    text += f"\n\n## Page {page_num + 1}\n\n"
                    text += page_text
    except Exception as e:
        print(f"PyPDF2 extraction failed: {e}")
    return text

def extract_text_pdfplumber(pdf_path):
    """Extract text using pdfplumber (better formatting)"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text and page_text.strip():
                    text += f"\n\n## Page {page_num + 1}\n\n"
                    text += page_text
    except Exception as e:
        print(f"pdfplumber extraction failed: {e}")
    return text

def clean_and_format_text(text):
    """Clean and format extracted text for markdown"""
    # Remove excessive whitespace
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
    
    # Fix common formatting issues
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Add space between words
    text = re.sub(r'\s+', ' ', text)  # Multiple spaces to single space
    
    # Try to identify headers (lines in all caps or with specific patterns)
    lines = text.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            formatted_lines.append('')
            continue
            
        # Check if line might be a header
        if (len(line) > 3 and len(line) < 80 and 
            (line.isupper() or 
             re.match(r'^[A-Z][^.]*$', line) or
             re.match(r'^\d+\.?\s+[A-Z]', line))):
            formatted_lines.append(f"\n### {line}\n")
        else:
            formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def convert_pdf_to_markdown(pdf_path, output_path=None):
    """Convert PDF to markdown format"""
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        return False
    
    if output_path is None:
        output_path = pdf_path.with_suffix('.md')
    else:
        output_path = Path(output_path)
    
    print(f"Converting {pdf_path} to {output_path}")
    
    # Try pdfplumber first (better formatting)
    text = extract_text_pdfplumber(pdf_path)
    
    # Fallback to PyPDF2 if pdfplumber fails
    if not text.strip():
        print("Trying PyPDF2 as fallback...")
        text = extract_text_pypdf2(pdf_path)
    
    if not text.strip():
        print("Error: Could not extract text from PDF")
        return False
    
    # Clean and format the text
    formatted_text = clean_and_format_text(text)
    
    # Create markdown header
    markdown_content = f"""# {pdf_path.stem}

**Source**: {pdf_path.name}  
**Converted**: {Path(__file__).parent}  
**Extraction Method**: {'pdfplumber' if 'pdfplumber' in text else 'PyPDF2'}

---

{formatted_text}

---

*Converted from PDF to Markdown for analysis purposes*
"""
    
    # Write to markdown file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Successfully converted to {output_path}")
        print(f"Extracted {len(text)} characters, formatted to {len(markdown_content)} characters")
        return True
    except Exception as e:
        print(f"Error writing markdown file: {e}")
        return False

if __name__ == "__main__":
    # Convert both DBA handbooks
    current_handbook = "papers/DBAHandbook.pdf"
    old_handbook = "papers/649DBA Handbook 2019-2020.pdf"
    
    print("Converting DBA Handbooks to Markdown...")
    
    # Convert new handbook
    if Path(current_handbook).exists():
        convert_pdf_to_markdown(current_handbook, "papers/DBAHandbook.md")
    else:
        print(f"New handbook not found: {current_handbook}")
    
    # Convert old handbook for comparison
    if Path(old_handbook).exists():
        convert_pdf_to_markdown(old_handbook, "papers/DBAHandbook-2019-2020.md")
    else:
        print(f"Old handbook not found: {old_handbook}")
    
    print("Conversion complete!")
