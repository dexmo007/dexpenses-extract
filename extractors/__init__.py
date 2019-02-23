class Extractor:
    def __init__(self, field):
        self.field = field

    def extract(self, text, lines, extracted):
        """extract this field value from the text"""
        raise NotImplementedError


class DependentExtractor(Extractor):
    def __init__(self, field, after):
        super().__init__(field)
        self.after = after


def extract(text, extractors):
    extracted = {}
    lines = text.splitlines()
    for extractor in extractors:
        extracted_value = extractor.extract(text, lines, extracted)
        extracted[extractor.field] = extracted_value
    return extracted
