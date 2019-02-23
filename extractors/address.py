import re
import googlemaps
from extractors import DependentExtractor
from extractors.header import HeaderExtractor


class AddressExtractor(DependentExtractor):

    def __init__(self, gmaps_key):
        super().__init__('address', after=HeaderExtractor)
        self.gmaps = googlemaps.Client(key=gmaps_key)

    def extract(self, text, lines, extracted):
        return self.gmaps.geocode(', '.join(extracted['header']))
