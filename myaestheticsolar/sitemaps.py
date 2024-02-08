from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'contact','services','service_detail','portfolio','process']

    def location(self, items):
        return reverse(items)
