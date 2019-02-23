import inspect
from extractors import DependentExtractor
from extractors import Extractor


def init(extractors):
    ordered_extractors = []
    dep = []
    for extractor in extractors:
        if isinstance(extractor, DependentExtractor) and extractor.after:
            dep.append(extractor)
        else:
            ordered_extractors.append(extractor)

    def contains_cls(_cls):
        return any([isinstance(oe, _cls) for oe in ordered_extractors])

    def _handle_dependent_extractors(rest):
        if not rest:
            return
        new_rest = []
        for de in rest:
            if inspect.isclass(de.after):
                if contains_cls(de.after):
                    ordered_extractors.append(de)
                else:
                    new_rest.append(de)
            else:
                if all([contains_cls(a) for a in de.after]):
                    ordered_extractors.append(de)
                else:
                    new_rest.append(de)
        return _handle_dependent_extractors(new_rest)

    _handle_dependent_extractors(dep)

    return ordered_extractors
