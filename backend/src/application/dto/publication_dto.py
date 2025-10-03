""" DTO para la entidad Publicación """
from typing import List, Optional

from pydantic import BaseModel, Field

from ...domain.entities.publication import PubType


class PublicationDTO(BaseModel):
    """ DTO base de una publicación. """
    pub_title: str
    pub_year: int
    pub_affiliation: str
    pub_type: PubType
    doi: str
    source: str


class PublicationUpdateDTO(BaseModel):
    """ DTO para actualizar una publicación. """
    pub_title: Optional[str] = Field(None, description="Título de la publicación")
    pub_year: Optional[int] = Field(None, description="Año de publicación")
    pub_affiliation: Optional[str] = Field(None, description="Afiliación de la publicación")
    pub_type: Optional[PubType] = Field(None, description="Tipo de publicación")
    source: Optional[str] = Field(None, description="Fuente de la publicación")


class PublicationsResponseDTO(BaseModel):
    """ DTO de respuesta de una publicación. """
    scopus_account: str
    publications: List[PublicationDTO]
