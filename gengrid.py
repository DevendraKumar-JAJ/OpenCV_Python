# fixed_popup_pdf.py

pdf = """%PDF-1.7
1 0 obj
<<
  /Type /Catalog
  /OpenAction 2 0 R
  /Pages 3 0 R
  /AcroForm <<
    /Fields [5 0 R]
    /DA (/Helv 0 Tf 0 g)
    /DR <<
      /Font <<
        /Helv 7 0 R
      >>
    >>
  >>
>>
endobj

2 0 obj
<<
  /S /JavaScript
  /JS (
    var name = app.response("Enter your name:", "User Input");
    if (name != null) {
      this.getField("output").value = "Hello, " + name + "!";
    }
  )
>>
endobj

3 0 obj
<<
  /Type /Pages
  /Kids [4 0 R]
  /Count 1
>>
endobj

4 0 obj
<<
  /Type /Page
  /Parent 3 0 R
  /MediaBox [0 0 612 792]
  /Annots [5 0 R]
  /Contents 6 0 R
  /Resources <<
    /Font <<
      /Helv 7 0 R
    >>
  >>
>>
endobj

5 0 obj
<<
  /FT /Tx
  /T (output)
  /Rect [200 400 400 430]
  /Subtype /Widget
  /Type /Annot
  /DA (/Helv 12 Tf 0 g)
  /F 4
  /MK << >>
>>
endobj

6 0 obj
<< >>
stream
BT
/Helv 18 Tf
72 700 Td
(User Input Demo) Tj
ET
endstream
endobj

7 0 obj
<<
  /Type /Font
  /Subtype /Type1
  /BaseFont /Helvetica
>>
endobj

trailer
<<
  /Root 1 0 R
  /Size 8
>>
%%EOF
"""

with open("popup_input_fixed.pdf", "w") as f:
    f.write(pdf)

print("✅ Created popup_input_fixed.pdf — open it in Adobe Acrobat Reader.")
