# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils.encoding import smart_str, smart_unicode
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document
from .forms import DocumentForm

from django.http import HttpResponse
import csv

try:
        import Image
except ImportError:
        from PIL import Image
import pytesseract

global i
i = 0
k=None
def list(request):
    global i,k

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            i += 1

            d = Document.objects.get(id=i)


            k=pytesseract.image_to_string(Image.open(d.docfile))
            k=smart_str(k)
            k.split()
            handle = open('ocr.txt', 'w+')
            handle.write(k)


            handle.close()

            '''txt_file = r"ocr.txt"
            csv_file = r'mycsv.csv'

            in_txt = csv.reader(open(txt_file, "rb"), delimiter = ' ')
            out_csv = csv.writer(open(csv_file, 'wb'))

            out_csv.writerows(in_txt.encode("utf-8"))'''



            return HttpResponseRedirect(list)
    else:
        form = DocumentForm()


    documents = Document.objects.all()


    return render(
        request,
        'ocr/show.html',
        {'documents': documents, 'form': form,'fl':k}

    )
