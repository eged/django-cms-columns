from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings
from django.utils.html import strip_tags
from django.utils.text import truncate_words

from cms.models import CMSPlugin
from cms.plugins.text.models import AbstractText
from cms.plugins.text.utils import plugin_admin_html_to_tags, plugin_tags_to_admin_html

from cms_columns import app_settings 

class AbstractColumn(models.Model):
    column_width = models.CharField(_("Column width"), max_length=6, choices=app_settings.get('CMS_COLUMNS_WIDTH_CHOICES'), default='100', null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        result = self.column_width.__str__()+"%";
        return result + " ] [ "+u" %s" % (truncate_words(strip_tags(self.body), 3)[:30]+"...")

class TextColumn(AbstractText):
    pass

class ManualBreak(CMSPlugin):
    column_width = '100'
    
    def __unicode__(self):
        return u'%s' % self.column_width

CMS_VISUAL_BREAK_OPTIONS = getattr(settings, 'CMS_VISUAL_BREAK_OPTIONS', (
                                                        ('vertical-space', _('Vertical Space')),
                                                        ('visual-break', _('Visual Break')),
                                                    )
                                        )
class VisualBreak(CMSPlugin):
    css_class = models.CharField(_("CSS Class"), max_length=100, default="visual-break", blank=True, choices=CMS_VISUAL_BREAK_OPTIONS)
    
    def __unicode__(self):
        return u'%s' % self.css_class
