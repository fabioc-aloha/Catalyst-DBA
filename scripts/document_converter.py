#!/usr/bin/env python3
"""
Document to Markdown Converter
==============================

Comprehensive converter for research documents supporting:
- PDF files (academic papers, handbooks)
- DOCX files (research proposals, manuscripts)
- Batch processing for entire directories
- Intelligent text cleaning and markdown formatting

Author: Alex Finch (AI Research Partner)
Project: AIRS - AI Readiness Score Development
Purpose: Enable systematic analysis of 100+ research documents
"""

import os
import sys
import argparse
from pathlib import Path
import re
from typing import Optional, List, Dict, Tuple

# PDF processing imports
try:
    import pdfplumber
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    print("⚠️  PDF libraries not available. Install with: pip install pdfplumber PyPDF2")

# DOCX processing imports
try:
    from docx import Document
    import docx2txt
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False
    print("⚠️  DOCX libraries not available. Install with: pip install python-docx docx2txt")

class DocumentConverter:
    """
    Multi-format document converter optimized for academic research.
    
    Features:
    - Intelligent PDF extraction with fallback methods
    - DOCX processing with formatting preservation
    - Academic citation and reference handling
    - Batch processing capabilities
    - Error logging and recovery
    """
    
    def __init__(self, output_dir: str = None):
        self.output_dir = Path(output_dir) if output_dir else None
        if self.output_dir:
            self.output_dir.mkdir(exist_ok=True)
        self.conversion_log = []
        
    def convert_pdf(self, pdf_path: str) -> Tuple[bool, str, str]:
        """
        Convert PDF to markdown with dual-library approach.
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            Tuple of (success, markdown_content, error_message)
        """
        if not PDF_AVAILABLE:
            return False, "", "PDF libraries not installed"
            
        pdf_path = Path(pdf_path)
        markdown_content = ""
        
        try:
            # Primary method: pdfplumber (better for academic papers)
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    text = page.extract_text()
                    if text:
                        markdown_content += f"\n\n## Page {page_num}\n\n{text}"
                        
            if markdown_content:
                return True, self._clean_text(markdown_content), ""
                
        except Exception as e:
            print(f"⚠️  pdfplumber failed for {pdf_path.name}: {e}")
            
        try:
            # Fallback method: PyPDF2
            markdown_content = ""
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page_num, page in enumerate(reader.pages, 1):
                    text = page.extract_text()
                    if text:
                        markdown_content += f"\n\n## Page {page_num}\n\n{text}"
                        
            if markdown_content:
                return True, self._clean_text(markdown_content), ""
                
        except Exception as e:
            return False, "", f"Both PDF extraction methods failed: {e}"
            
        return False, "", "No text content extracted"
    
    def convert_docx(self, docx_path: str) -> Tuple[bool, str, str]:
        """
        Convert DOCX to markdown preserving structure.
        
        Args:
            docx_path: Path to DOCX file
            
        Returns:
            Tuple of (success, markdown_content, error_message)
        """
        if not DOCX_AVAILABLE:
            return False, "", "DOCX libraries not installed"
            
        docx_path = Path(docx_path)
        
        try:
            # Primary method: python-docx (better structure preservation)
            doc = Document(docx_path)
            markdown_content = f"# {docx_path.stem}\n\n"
            
            for paragraph in doc.paragraphs:
                text = paragraph.text.strip()
                if not text:
                    continue
                    
                # Handle headings based on style
                style = paragraph.style.name.lower()
                if 'heading 1' in style or 'title' in style:
                    markdown_content += f"\n# {text}\n\n"
                elif 'heading 2' in style:
                    markdown_content += f"\n## {text}\n\n"
                elif 'heading 3' in style:
                    markdown_content += f"\n### {text}\n\n"
                elif 'heading' in style:
                    markdown_content += f"\n#### {text}\n\n"
                else:
                    markdown_content += f"{text}\n\n"
                    
            return True, self._clean_text(markdown_content), ""
            
        except Exception as e:
            print(f"⚠️  python-docx failed for {docx_path.name}: {e}")
            
        try:
            # Fallback method: docx2txt (simpler but reliable)
            text = docx2txt.process(docx_path)
            if text:
                markdown_content = f"# {docx_path.stem}\n\n{text}"
                return True, self._clean_text(markdown_content), ""
                
        except Exception as e:
            return False, "", f"Both DOCX extraction methods failed: {e}"
            
        return False, "", "No text content extracted"
    
    def _clean_text(self, text: str) -> str:
        """
        Clean and optimize text for markdown format.
        
        Academic document specific cleaning:
        - Remove excessive whitespace
        - Fix line breaks
        - Preserve citations and references
        - Handle special characters
        """
        # Remove excessive whitespace but preserve paragraph breaks
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r'[ \t]+', ' ', text)
        
        # Fix common PDF extraction issues
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # camelCase fixes
        text = re.sub(r'(\.)([A-Z])', r'\1 \2', text)     # Period spacing
        
        # Preserve academic citations (Author, Year) format
        text = re.sub(r'\(\s*([A-Za-z]+)\s*,\s*(\d{4})\s*\)', r'(\1, \2)', text)
        
        # Clean up common OCR artifacts
        text = re.sub(r'[^\w\s\-\(\).,;:!?\'\"\/\\\[\]{}]', '', text)
        
        return text.strip()
    
    def convert_document(self, file_path: str) -> bool:
        """
        Convert single document to markdown.
        
        Args:
            file_path: Path to document file
            
        Returns:
            True if conversion successful
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            return False
            
        # Determine conversion method
        suffix = file_path.suffix.lower()
        
        if suffix == '.pdf':
            success, content, error = self.convert_pdf(file_path)
        elif suffix in ['.docx', '.doc']:
            success, content, error = self.convert_docx(file_path)
        else:
            print(f"❌ Unsupported file format: {suffix}")
            return False
            
        if not success:
            print(f"❌ Conversion failed for {file_path.name}: {error}")
            self.conversion_log.append({
                'file': str(file_path),
                'status': 'failed',
                'error': error
            })
            return False
            
        # Save markdown file in same directory as original (or specified output dir)
        if self.output_dir:
            output_file = self.output_dir / f"{file_path.stem}.md"
        else:
            output_file = file_path.parent / f"{file_path.stem}.md"
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"✅ Converted: {file_path.name} → {output_file.name}")
            self.conversion_log.append({
                'file': str(file_path),
                'output': str(output_file),
                'status': 'success',
                'size': len(content)
            })
            return True
            
        except Exception as e:
            print(f"❌ Failed to save {output_file}: {e}")
            return False
    
    def batch_convert(self, directory: str, file_pattern: str = "*") -> Dict[str, int]:
        """
        Convert all documents in directory.
        
        Args:
            directory: Directory to scan
            file_pattern: Glob pattern for files
            
        Returns:
            Dictionary with conversion statistics
        """
        directory = Path(directory)
        
        if not directory.exists():
            print(f"❌ Directory not found: {directory}")
            return {'total': 0, 'success': 0, 'failed': 0}
            
        # Find all supported documents
        supported_extensions = ['.pdf', '.docx', '.doc']
        files = []
        
        for ext in supported_extensions:
            files.extend(directory.rglob(f"{file_pattern}{ext}"))
            
        print(f"\n🔍 Found {len(files)} documents to convert in {directory}")
        
        stats = {'total': len(files), 'success': 0, 'failed': 0}
        
        for file_path in files:
            if self.convert_document(file_path):
                stats['success'] += 1
            else:
                stats['failed'] += 1
                
        return stats
    
    def print_summary(self):
        """Print conversion summary and statistics."""
        if not self.conversion_log:
            print("\n📊 No conversions performed.")
            return
            
        successful = [entry for entry in self.conversion_log if entry['status'] == 'success']
        failed = [entry for entry in self.conversion_log if entry['status'] == 'failed']
        
        print(f"\n📊 Conversion Summary:")
        print(f"   ✅ Successful: {len(successful)}")
        print(f"   ❌ Failed: {len(failed)}")
        
        if successful:
            total_size = sum(entry['size'] for entry in successful)
            print(f"   📝 Total content: {total_size:,} characters")
            if self.output_dir:
                print(f"   📁 Output directory: {self.output_dir}")
            else:
                print(f"   📁 Files saved alongside originals")
            
        if failed:
            print(f"\n❌ Failed conversions:")
            for entry in failed[:5]:  # Show first 5 failures
                print(f"   - {Path(entry['file']).name}: {entry['error']}")
            if len(failed) > 5:
                print(f"   ... and {len(failed) - 5} more")

def main():
    """Command-line interface for document conversion."""
    parser = argparse.ArgumentParser(
        description="Convert PDF and DOCX documents to Markdown for research analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert single file (saves .md alongside original)
  python document_converter.py file.pdf
  
  # Convert all documents in papers directory (saves .md files alongside originals)
  python document_converter.py --batch papers/
  
  # Convert with custom output directory
  python document_converter.py --batch papers/ --output converted_papers/
  
  # Convert specific pattern
  python document_converter.py --batch papers/ --pattern "*AIRS*"
        """
    )
    
    parser.add_argument('input', nargs='?', help='Input file or directory')
    parser.add_argument('--batch', metavar='DIR', help='Batch convert directory')
    parser.add_argument('--output', metavar='DIR', default=None, 
                       help='Output directory (default: same as source file)')
    parser.add_argument('--pattern', metavar='PATTERN', default='*',
                       help='File pattern for batch mode (default: *)')
    
    args = parser.parse_args()
    
    if not args.input and not args.batch:
        parser.print_help()
        return
        
    # Check dependencies
    if not PDF_AVAILABLE and not DOCX_AVAILABLE:
        print("❌ No document processing libraries available!")
        print("📦 Install with: pip install -r requirements.txt")
        return
        
    converter = DocumentConverter(args.output)
    
    if args.batch:
        # Batch conversion mode
        stats = converter.batch_convert(args.batch, args.pattern)
        converter.print_summary()
        
    elif args.input:
        # Single file conversion mode
        converter.convert_document(args.input)
        converter.print_summary()
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
