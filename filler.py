import sys
import pdfrw
import json
from datetime import date

INVOICE_TEMPLATE_PATH = 'templates/28MODEL Declaratie proprie raspundere 2503.pdf'
INVOICE_OUTPUT_PATH = 'output/declaratie.pdf'

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict, signature_path):
    pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    if data_dict[key] == '/YES':
                        annotation.update(pdfrw.PdfDict(AS=pdfrw.PdfName('On'), V=pdfrw.PdfName('On')))
                    else:
                        annotation.update(
                            pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                        )

    sgn = pdfrw.PageMerge().add(pdfrw.PdfReader(signature_path).pages[0])[0]
    sgn.scale(0.3)
    sgn.y += 100
    sgn.x += 380

    pdfrw.PageMerge(pdf.pages[0]).add(sgn, prepend='underneath').render()

    pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write(output_pdf_path, pdf)


persons = json.load(open('data/persons.json'))
data_d = None
signature = None

name = sys.argv[1]

for p in persons['people']:
    if p['username'] == name:
        data_d = p
        for (k, v) in data_d.items():
            if v == '$date':
                data_d[k] = date.today()
        signature = 'data/signatures/' + p['signature']


reasons = json.load(open('data/reasons.json'))
reason = sys.argv[2]

for p in reasons['reasons']:
    if p['activity'] == reason:
        data_d.update(p)

write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_d, signature)
