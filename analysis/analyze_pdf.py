import os
import PyPDF2
import language_tool_python

# المجلدات
input_folder = "input"
output_folder = "output"
input_file = "sample.pdf"  # اسم ملف PDF
output_file = "sample_corrected.txt"

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def correct_text(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected = language_tool_python.utils.correct(text, matches)
    return corrected

if __name__ == "__main__":
    input_path = os.path.join(input_folder, input_file)
    output_path = os.path.join(output_folder, output_file)

    # استخراج النص
    extracted = extract_text_from_pdf(input_path)

    # التصحيح
    corrected = correct_text(extracted)

    # حفظ النتيجة
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(corrected)

    print(f"✅ تم حفظ النص المصحّح في: {output_path}")
