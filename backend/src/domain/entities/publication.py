""" Módulo que define la entidad de Publicación. """
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional

MIN_YEAR = 1900

class PubType(str, Enum):
    """ Enum que representa el tipo de publicación. """
    ARTICLE = "Article"
    CONFERENCE = "Conference Paper"
    REVIEW = "Review"
    BOOK_CHAPTER = "Book Chapter"
    EDITORIAL = "Editorial"
    ERRATUM = "Erratum"
    NOTE = "Note"
    PAPER = "Data Paper"
    BOOK = "Book"
    OTHER = "Other"


@dataclass
class Publication:
    """ Entidad que representa una publicación. """
    pub_id: Optional[int]
    pub_title: str
    pub_year: int
    pub_affiliation: str
    pub_type: PubType
    doi: str
    source: str
    scopus_id: str

    def is_valid(self) -> bool:
        """ Valida que la publicación tenga los campos obligatorios. """
        return (
            bool(self.pub_title and self.pub_title.strip()) and
            bool(self.pub_year and self.is_year_valid()) and
            bool(self.pub_affiliation and self.pub_affiliation.strip()) and
            bool(self.pub_type and self.pub_type in PubType) and
            bool(self.doi and self.doi.strip() and self.doi.startswith("10.")) and
            bool(self.source and self.source.strip()) and
            bool(self.scopus_id and self.scopus_id.strip())
        )

    def is_year_valid(self) -> bool:
        """ Valida que el año de publicación se encuentre dentro del rango establecido. """
        return MIN_YEAR <= self.pub_year <= date.today().year