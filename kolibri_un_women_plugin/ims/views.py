from django.views.generic.base import TemplateView

from kolibri.content.models import ChannelMetadata

class ThinCommonCartridgeManifestView(TemplateView):

    template_name = "ims/ccthin/manifest.xml"

    def get_context_data(self, **kwargs):
        context = super(ThinCommonCartridgeManifestView, self).get_context_data(**kwargs)
        context["baseurl"] = self.request.build_absolute_uri("/")
        context['channels'] = ChannelMetadata.objects.all()
        return context