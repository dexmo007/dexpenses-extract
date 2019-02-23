import sys
import os
from dotenv import load_dotenv
from ocr import ocr
import extractors
from extractors.date import DateExtractor
from extractors.time import TimeExtractor
from extractors.amount import AmountExtractor
from extractors.payment_method import PaymentMethodExtractor
from extractors.header import HeaderExtractor
from extractors.address import AddressExtractor
from extractors.category import StaticCategoryExtractor
from extractors import engine

load_dotenv()

EXTRACTORS = [DateExtractor(), TimeExtractor(), AmountExtractor(), PaymentMethodExtractor(),
              HeaderExtractor(), AddressExtractor(gmaps_key=os.getenv('GMAPS_API_KEY')), StaticCategoryExtractor()]

text = ocr(sys.argv[1], preprocess=None, lang='deu')
print(text)
extracted = extractors.extract(
    text, engine.init(EXTRACTORS))

print(extracted)
