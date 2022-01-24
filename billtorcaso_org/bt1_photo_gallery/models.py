from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtail_photo_gallery.models import GalleryBlock, ImageGalleryMixin

class BT1PhotoGallery(ImageGalleryMixin, Page):

    intro = models.CharField(max_length=250)
    content = StreamField([
        ("gallery", GalleryBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel("content"),
    ]
