# external
import xhtml2pdf.pisa as pisa

source_html = open('index.html', 'r').read()
output_filename = 'citrushack.pdf'

# Enable pisa logging
pisa.showLogging()

# Compile HTML to PDF
with open(output_filename, 'w') as result_file:
    pisa_status = pisa.CreatePDF(source_html, result_file)

# Print error if it occurred, otherwise print success
if pisa_status.err == False:
    print 'Compilation successful'
else:
    print 'Compilation failed'

