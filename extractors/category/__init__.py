import re
import os
from dotenv import dotenv_values
from extractors import DependentExtractor
from extractors.header import HeaderExtractor
from extractors.address import AddressExtractor


def load_place_type_mappings():
    return dotenv_values(dotenv_path=os.path.join(os.path.dirname(__file__), 'gmaps_place_types.env'))


class StaticCategoryExtractor(DependentExtractor):

    def __init__(self):
        super().__init__('category', after=[HeaderExtractor, AddressExtractor])
        self.place_type_mappings = load_place_type_mappings()

    def _map_place_types(self, types):
        for _type in types:
            if _type not in self.place_type_mappings or not self.place_type_mappings[_type]:
                yield {
                    'category': _type,
                    'category_type': 'unknown'
                }
            else:
                yield {
                    'category': _type,
                    'category_type': self.place_type_mappings[_type]
                }

    def extract(self, text, lines, extracted):
        address = extracted['address']
        if address and len(address) == 1 and 'types' in address[0]:
            return list(self._map_place_types(address[0]['types']))

        return None
