import re
from dataclasses import dataclass
from extractors import Extractor


@dataclass
class Amount:
    value: float
    currency: str = 'EUR'


class AmountExtractor(Extractor):
    def __init__(self):
        super().__init__('amount')

    def extract(self, text: str, lines, extracted):
        for line in lines:
            m = re.match(r'^(?i)betrag\s*(?:EUR)?\s*(\d+,\d\d).*$', line)
            if m:
                return Amount(float(m.group(1).replace(',', '.')))
