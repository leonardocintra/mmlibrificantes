from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class ContatoView(TemplateView):
    template_name = 'contato.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'


index = IndexView.as_view()
contato = ContatoView.as_view()
sobre = SobreView.as_view()