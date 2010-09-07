from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.plugins.text.cms_plugins import TextPlugin

from cms_columns.models import TextColumn, ManualBreak, VisualBreak

class TextColumnPlugin(TextPlugin):
    model = TextColumn
    name = _("Text column")
    admin_preview = False

class ManualBreakPlugin(CMSPluginBase):
    model = ManualBreak
    name = _("Manual break")
    admin_preview = False
    render_plugin = False

    def render(self, context, instance, placeholder):
        return context

class VisualBreakPlugin(CMSPluginBase):
    model = VisualBreak
    name = _("Visual break")
    admin_preview = False
    render_template = "cms_columns/visual_break.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'css_class': instance.css_class,
            'placeholder': placeholder,
        })
        return context
            
plugin_pool.register_plugin(TextColumnPlugin)
plugin_pool.register_plugin(ManualBreakPlugin)
plugin_pool.register_plugin(VisualBreakPlugin)
