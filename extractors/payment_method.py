import re
from extractors import Extractor

regexes = {
    'debit': [
        r'^\s*girocard\s*$'
    ]
}


def any_match(line):
    for payment_method, identifiers in regexes.items():
        for identifier in identifiers:
            if re.match(identifier, line):
                return payment_method
    return None


class PaymentMethodExtractor(Extractor):

    def __init__(self):
        super().__init__('payment_method')

    def extract(self, text, lines, extracted):
        for line in lines:
            m = any_match(line)
            if m:
                return m
        return None
