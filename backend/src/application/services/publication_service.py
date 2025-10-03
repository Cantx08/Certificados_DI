""" Módulo de servicios para la gestión de publicaciones. """
from typing import List

from ..dto.publication_dto import PublicationsResponseDTO, PublicationDTO, PublicationUpdateDTO
from ...domain.repositories.publication_repository import IPublicationRepository


class PublicationService:
    """ Servicio para la gestión de publicaciones. """

    def __init__(self, publication_repository: IPublicationRepository):
        self.publication_repository = publication_repository

    def get_publications_by_scopus_id(self, scopus_id: str) -> List[PublicationsResponseDTO]:
        """ Obtiene todas las publicaciones por el Scopus ID. """
        publications = self.publication_repository.get_by_scopus_id(scopus_id)
        publication_list = [
            PublicationDTO(
                pub_title=pub.pub_title,
                pub_year=pub.pub_year,
                pub_affiliation=pub.pub_affiliation,
                pub_type=pub.pub_type,
                doi=pub.doi,
                source=pub.source
            ) for pub in publications
        ]
        return [
            PublicationsResponseDTO(
                scopus_account=pub.scopus_id,
                publications=publication_list
            )
            for pub in publications
        ]

    def update_publication(self, pub_id: int, dto: PublicationUpdateDTO) -> PublicationDTO:
        """ Actualiza una publicación existente. """
        publication = self.publication_repository.get_by_id(pub_id)
        if not publication:
            raise ValueError("Publicación no encontrada")

        if dto.pub_title:
            publication.pub_title = dto.pub_title
        if dto.pub_year:
            publication.pub_year = dto.pub_year
        if dto.pub_affiliation:
            publication.pub_affiliation = dto.pub_affiliation
        if dto.pub_type:
            publication.pub_type = dto.pub_type
        if dto.source:
            publication.source = dto.source

        updated_publication = self.publication_repository.update(publication)
        return PublicationDTO(
            pub_title=updated_publication.pub_title,
            pub_year=updated_publication.pub_year,
            pub_affiliation=updated_publication.pub_affiliation,
            pub_type=updated_publication.pub_type,
            doi=updated_publication.doi,
            source=updated_publication.source
        )

    def delete_publication(self, pub_id: int) -> None:
        """ Elimina una publicación existente. """
        publication = self.publication_repository.get_by_id(pub_id)
        if not publication:
            raise ValueError("Publicación no encontrada")

        self.publication_repository.delete(pub_id)
