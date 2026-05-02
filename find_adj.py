import PyPDF2
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pdf_path = r'c:\Users\YACHI\Documents\Antigravity\French\法文筆記.pdf'

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total = len(reader.pages)
        print(f"Total pages: {total}")
        
        # Search all pages for adjective-related content
        keywords = ['形容詞', 'adjectif', 'grand', 'petit', 'beau', 'bon', 'nouveau']
        
        for i in range(total):
            page = reader.pages[i]
            text = page.extract_text()
            if text:
                for kw in keywords:
                    if kw.lower() in text.lower():
                        print(f"\n=== Page {i+1} (keyword: '{kw}') ===")
                        print(text[:300])
                        break

except Exception as e:
    print(f"Error: {e}")
