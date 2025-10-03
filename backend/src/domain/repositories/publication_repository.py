""" Interfaz para el repositorio de publicaciones. """
from abc import ABC, abstractmethod
from typing import List

from ..entities.publication import Publication


class PublicationRepository(ABC):
    """ Interfaz para el repositorio de publicaciones. """
    @abstractmethod
    def get_by_scopus_id(self, scopus_id: str) -> List[Publication]:
        """ Obtiene todas las publicaciones por el Scopus ID. """
        pass

    @abstractmethod
    def update(self, publication: Publication) -> Publication:
        """ Actualiza una publicación extraída. """
        pass

    @abstractmethod
    def delete(self, pub_id: int) -> None:
        """ Elimina una publicación extraída. """
        pass