from django.http import HttpResponse
from django.template import Template, Context


def formulario(request):

    doc_form = open('testsite/doc.html')
    plantilla = Template(doc_form.read())
    doc_form.close()
    ctx = Context()
    documento = plantilla.render(ctx)

    return HttpResponse(documento)


