import re
import datetime
from extractors import Extractor


class DateExtractor(Extractor):

    def __init__(self):
        super().__init__('date')

    def extract(self, text, lines, extracted):
        for line in lines:
            m = re.match(r'(?i)^datum\s*:?\s*(\d\d)\.(\d\d)\.(\d{4})$', line)
            if m:
                return datetime.datetime(day=int(m.group(1)), month=int(m.group(2)), year=int(m.group(3)))
        return None
