from typing import Set


def parse_accept_language(header: str, supported_languages: Set[str]) -> Set[str]:
    languages_in_header = [lang.strip() for lang in header.split(",")]

    def verify(lang):
        return lang in supported_languages

    return filter(verify, languages_in_header)
