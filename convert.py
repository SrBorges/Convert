# -*- coding:UTF-8 -*-

import sys
import os
from pdf2docx import Converter
import aspose.words as aw



def pdf2doc():
    arquivo = sys.argv[2]

    pdf = arquivo

    docx = ''

    cv = Converter(pdf)
    cv.convert(docx)
    cv.close()

    print("concluído... ")




def help():
    print(" -cf -> Converter PDF para DocX. \n")
    print(" -cx -> Converter ODT para PDF. \n")
    print(" -cp -> Converter ODT para DocX. \n ")
    print(" -ce -> Converter DocX para ODT. \n")


def doc2pdf():
    arquivo = sys.argv[2]

    doc = aw.Document(arquivo)

    doc.save("New.pdf")

    print("concluído... ")


def odt2doc():
    arquivo = sys.argv[2]

    doc = aw.Document(arquivo)

    doc.save("New.docx")

    print("concluído... ")

def doc2odt():
    arquivo = sys.argv[2]

    doc = aw.Document(arquivo)

    doc.save("New.odt")

    print("concluído...")



if __name__ == '__main__':
    opt = sys.argv[1]

    if opt == '-h':
        help()

    elif opt == '-cf':
        pdf2doc()

    elif opt == '-cx':
        doc2pdf()

    elif opt == '-cp':
        odt2doc()

    elif opt == '-ce':
        doc2odt()

    else:
        print("parâmetro inexistente. ")
