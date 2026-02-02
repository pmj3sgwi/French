import PyPDF2
import sys
import io

# Set stdout to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pdf_path = r'c:\Users\YACHI\Documents\Antigravity\French\法文筆記_L1-L3.pdf'
output_path = r'c:\Users\YACHI\Documents\Antigravity\French\pdf_content.txt'

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        content = []
        content.append(f"Total pages in PDF: {len(reader.pages)}\n")
        
        # Extract pages 8-15 (for Lesson 2) - 0-indexed so 7-14
        content.append("=" * 60)
        content.append("LESSON 2 (Pages 8-15)")
        content.append("=" * 60)
        for page_num in range(7, min(15, len(reader.pages))):
            page = reader.pages[page_num]
            content.append(f"\n--- Page {page_num + 1} ---")
            content.append(page.extract_text())
        
        # Extract pages 17-23 (for Lesson 1) - 0-indexed so 16-22
        content.append("\n" + "=" * 60)
        content.append("LESSON 1 (Pages 17-23)")
        content.append("=" * 60)
        for page_num in range(16, min(23, len(reader.pages))):
            page = reader.pages[page_num]
            content.append(f"\n--- Page {page_num + 1} ---")
            content.append(page.extract_text())
        
        # Write to file with UTF-8 encoding
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write('\n'.join(content))
        
        print(f"Successfully extracted content to {output_path}")
        
except Exception as e:
    print(f"Error: {e}")
