#!/usr/bin/env python3
"""
PDF Table Formatting Enhancer
============================

Post-processes converted markdown files to improve table formatting,
specifically designed for DBA Handbook and academic documents.

Author: Alex Finch (AI Research Partner)
Project: AIRS - DBA Research Enhancement
Purpose: Convert text-based tables to proper markdown table format
"""

import re
import sys
from pathlib import Path
from typing import List, Optional

class PDFTableEnhancer:
    """Enhances table formatting in markdown files converted from PDFs."""
    
    def __init__(self):
        self.table_patterns = [
            # DBA Course table pattern
            r'(DBA \d+\*?)\s+([^0-9\n]+?)\s+(\d+)',
            
            # Rubric table pattern (Excellent/Acceptable/Poor)
            r'### (Excellent)\s+(Acceptable)\s+(Poor)',
            
            # General three-column pattern
            r'([A-Za-z][^|\n]*?)\s+([A-Za-z][^|\n]*?)\s+([A-Za-z][^|\n]*?)(?=\n)',
        ]
    
    def enhance_file(self, file_path: str) -> bool:
        """
        Enhance table formatting in a markdown file.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            True if successfully enhanced, False otherwise
        """
        try:
            file_path_obj = Path(file_path)
            
            # Read the file
            with open(file_path_obj, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Enhance curriculum tables
            content = self._enhance_curriculum_tables(content)
            
            # Enhance rubric tables
            content = self._enhance_rubric_tables(content)
            
            # Clean up formatting
            content = self._clean_formatting(content)
            
            # Write back the enhanced content
            with open(file_path_obj, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Enhanced table formatting in {file_path_obj.name}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to enhance {file_path}: {e}")
            return False
    
    def _enhance_curriculum_tables(self, content: str) -> str:
        """Enhance DBA curriculum tables."""
        
        # Pattern for DBA course lines
        course_pattern = r'^(DBA \d+\*?)\s+(.+?)\s+(\d+)$'
        
        lines = content.split('\n')
        enhanced_lines = []
        in_curriculum_section = False
        table_buffer = []
        
        for line in lines:
            # Detect curriculum section
            if 'DOCTOR OF BUSINESS ADMINISTRATION (CURRICULUM)' in line:
                in_curriculum_section = True
                enhanced_lines.append(line)
                continue
            
            # End curriculum section
            if in_curriculum_section and line.startswith('---'):
                # Process any remaining table buffer
                if table_buffer:
                    enhanced_lines.extend(self._create_curriculum_table(table_buffer))
                    table_buffer = []
                in_curriculum_section = False
                enhanced_lines.append(line)
                continue
            
            if in_curriculum_section:
                # Check if this is a course line
                match = re.match(course_pattern, line)
                if match:
                    course_code, course_title, credits = match.groups()
                    table_buffer.append((course_code, course_title.strip(), credits))
                elif line.strip() and 'Core Courses' in line:
                    # Table header
                    if table_buffer:
                        enhanced_lines.extend(self._create_curriculum_table(table_buffer))
                        table_buffer = []
                    enhanced_lines.append(line)
                elif line.strip() and not line.startswith('*') and not line.startswith('Note'):
                    # Other content
                    if table_buffer:
                        enhanced_lines.extend(self._create_curriculum_table(table_buffer))
                        table_buffer = []
                    enhanced_lines.append(line)
                else:
                    enhanced_lines.append(line)
            else:
                enhanced_lines.append(line)
        
        # Process any remaining table buffer
        if table_buffer:
            enhanced_lines.extend(self._create_curriculum_table(table_buffer))
        
        return '\n'.join(enhanced_lines)
    
    def _create_curriculum_table(self, courses: List[tuple]) -> List[str]:
        """Create a proper markdown table from course data."""
        if not courses:
            return []
        
        table_lines = [
            "",
            "| Course Code | Course Title | Credit Hours |",
            "|-------------|--------------|--------------|"
        ]
        
        for course_code, course_title, credits in courses:
            table_lines.append(f"| {course_code} | {course_title} | {credits} |")
        
        table_lines.append("")
        return table_lines
    
    def _enhance_rubric_tables(self, content: str) -> str:
        """Enhance rubric tables with Excellent/Acceptable/Poor columns."""
        
        lines = content.split('\n')
        enhanced_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Check if this is a rubric header line
            if re.match(r'### (Excellent)\s+(Acceptable)\s+(Poor)', line):
                # Add proper table header
                enhanced_lines.append("")
                enhanced_lines.append("| Excellent | Acceptable | Poor |")
                enhanced_lines.append("|-----------|------------|------|")
                
                # Look ahead for the content rows
                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    
                    # Stop if we hit another section
                    if (next_line.startswith('#') or 
                        next_line.startswith('---') or 
                        next_line.strip() == '' or
                        'Touro University Worldwide' in next_line):
                        break
                    
                    # Try to parse as table content
                    table_row = self._parse_rubric_content(next_line)
                    if table_row:
                        enhanced_lines.append(table_row)
                    else:
                        # If we can't parse it as a table row, it might be continuation text
                        # Add it as regular content
                        enhanced_lines.append(next_line)
                    
                    i += 1
                
                # Don't increment i again since the while loop already did
                continue
            else:
                enhanced_lines.append(line)
                i += 1
        
        return '\n'.join(enhanced_lines)
    
    def _parse_rubric_content(self, line: str) -> Optional[str]:
        """Parse a line as rubric table content."""
        if not line.strip():
            return None
        
        # Skip lines that are clearly not table content
        if (line.startswith('#') or 
            line.startswith('---') or 
            'Touro University' in line or
            len(line.strip()) < 10):
            return None
        
        # Try to identify three distinct parts
        # Look for patterns like "text text text"
        
        # Method 1: Split on multiple spaces (2 or more)
        parts = re.split(r'\s{2,}', line.strip())
        if len(parts) >= 3:
            excellent = parts[0].strip()
            acceptable = parts[1].strip()
            poor = ' '.join(parts[2:]).strip()
            return f"| {excellent} | {acceptable} | {poor} |"
        
        # Method 2: Try to identify text blocks by content
        # Look for common patterns
        text = line.strip()
        
        # Pattern: "Clear, Articulated" type phrases
        patterns = [
            # Three distinct quality levels
            r'^(.+?)\s+(Clear|Sufficient|Minimal|Adequate|Acceptable|Good)\s*,?\s*(.+?)\s+((?:Not|Lacks|Insufficient|Poor|Scattered).+?)$',
            
            # Two quality levels (excellent merged with acceptable)
            r'^(.+?)\s+((?:Clear|Sufficient|Minimal|Adequate|Not|Lacks|Insufficient|Poor|Scattered).+?)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, text, re.IGNORECASE)
            if match:
                groups = match.groups()
                if len(groups) >= 3:
                    return f"| {groups[0].strip()} | {groups[1].strip()} | {groups[2].strip()} |"
                elif len(groups) == 2:
                    # Two columns - assume first is excellent, second is poor
                    return f"| {groups[0].strip()} | | {groups[1].strip()} |"
        
        # Method 3: If line contains quality indicators, try to split around them
        quality_words = ['clear', 'sufficient', 'minimal', 'adequate', 'lacks', 'insufficient', 'not', 'poor', 'scattered']
        for word in quality_words:
            if word in text.lower():
                # Try to split around this word
                word_pos = text.lower().find(word)
                if word_pos > 10:  # Ensure there's substantial text before
                    before = text[:word_pos].strip()
                    after = text[word_pos:].strip()
                    # This might be excellent | acceptable/poor combined
                    return f"| {before} | {after} | |"
        
        # If we can't parse it as a table, return None
        return None
    
    def _split_rubric_line(self, line: str) -> List[str]:
        """Split a rubric line into three columns."""
        # Remove extra whitespace
        line = ' '.join(line.split())
        
        # Common patterns for splitting rubric content
        patterns = [
            # Pattern: "text text text"
            r'^(.+?)\s+(.+?)\s+(.+?)$',
            
            # Pattern with qualifiers
            r'^(.+?)\s+(Clear|Sufficient|Minimal|No|Lacks|Obvious).+?\s+(.+?)$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                return [group.strip() for group in match.groups()]
        
        # Fallback: split on multiple spaces
        parts = re.split(r'\s{2,}', line)
        if len(parts) >= 3:
            return [parts[0].strip(), parts[1].strip(), ' '.join(parts[2:]).strip()]
        
        return [line.strip()]
    
    def _clean_formatting(self, content: str) -> str:
        """Clean up general formatting issues."""
        
        # Remove excessive blank lines
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        
        # Fix headers that got mangled
        content = re.sub(r'###\s+([A-Z][A-Za-z\s]+)\s+([A-Z][A-Za-z\s]+)\s+([A-Z][A-Za-z\s]+)', 
                        r'### \1\n### \2\n### \3', content)
        
        # Clean up table formatting
        content = re.sub(r'\|\s*\|\s*\|', '| | |', content)
        
        return content

def main():
    """Main function for command line usage."""
    if len(sys.argv) != 2:
        print("Usage: python pdf_table_enhancer.py <markdown_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    enhancer = PDFTableEnhancer()
    
    if enhancer.enhance_file(file_path):
        print("✅ Table enhancement completed successfully")
    else:
        print("❌ Table enhancement failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
