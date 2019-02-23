import re
import datetime
from extractors import Extractor


class TimeExtractor(Extractor):
    def __init__(self):
        super().__init__('time')

    def extract(self, text, lines, extracted):
        for line in lines:
            m = re.match(
                r'(?i)^.*(\d\d):(\d\d):(\d\d)\s*(?:uhr)?.*$', line)
            if m:
                return datetime.time(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        return None
