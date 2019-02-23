import re
import string
from typing import List
from dataclasses import dataclass
import googlemaps
from extractors import Extractor


class HeaderExtractor(Extractor):

    def __init__(self, max_header_lines=8):
        super().__init__('header')
        self.max_header_lines = max_header_lines

    def _is_irrelevant_title(self, line):
        return re.search(r'(?i)kundenbeleg|h(ae|ä)ndlerbeleg', line)

    def _is_header_delimiter(self, line: str):
        for c in line:
            if c in string.ascii_letters or c in string.digits:
                return False
        return True

    def extract(self, text, lines, extracted):
        header_lines = []
        for i, line in enumerate(lines):
            if i >= self.max_header_lines:
                break
            if self._is_irrelevant_title(line):
                continue
            if not line.strip() or self._is_header_delimiter(line):
                break
            header_lines.append(line)

        return header_lines
