from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from tp2_2227667.domain.exceptions import DonneesInvalidesError


class StatutMission(Enum):
    """États possibles d'une mission de transport."""

    PLANIFIEE = "planifiee"
    EN_COURS = "en_cours"
    LIVREE = "livree"
    ANNULEE = "annulee"


@dataclass
class MissionTransport:
    """Représente une mission pour transporter une commande."""

    identifiant: int
    commande_id: int
    chauffeur_id: int
    camion_id: int
    depart_prevu: datetime
    arrivee_prevue: datetime
    statut: StatutMission = StatutMission.PLANIFIEE
    depart_reel: datetime | None = None
    arrivee_reelle: datetime | None = None

    def __post_init__(self) -> None:
        """Valide les informations et les horaires de la mission."""
        if self.identifiant <= 0:
            raise DonneesInvalidesError(
                "L'identifiant de la mission doit être positif."
            )
        if self.commande_id <= 0:
            raise DonneesInvalidesError(
                "L'identifiant de la commande doit être positif."
            )
        if self.chauffeur_id <= 0 or self.camion_id <= 0:
            raise DonneesInvalidesError(
                "Les identifiants du chauffeur et du camion doivent être positifs."
            )
        if self.arrivee_prevue <= self.depart_prevu:
            raise DonneesInvalidesError(
                "L'arrivée prévue doit être après le départ prévu."
            )
        if self.arrivee_reelle is not None and self.depart_reel is None:
            raise DonneesInvalidesError(
                "Une arrivée réelle exige un départ réel."
            )
        if (
            self.arrivee_reelle is not None
            and self.depart_reel is not None
            and self.arrivee_reelle < self.depart_reel
        ):
            raise DonneesInvalidesError(
                "L'arrivée réelle ne peut pas précéder le départ réel."
            )

    def demarrer(self, instant: datetime) -> None:
        """Démarre une mission planifiée."""
        if self.statut is not StatutMission.PLANIFIEE:
            raise DonneesInvalidesError(
                "Seule une mission planifiée peut être démarrée."
            )
        self.depart_reel = instant
        self.statut = StatutMission.EN_COURS

    def terminer(self, instant: datetime) -> None:
        """Termine une mission en cours."""
        if self.statut is not StatutMission.EN_COURS:
            raise DonneesInvalidesError(
                "Seule une mission en cours peut être terminée."
            )
        if self.depart_reel is None or instant < self.depart_reel:
            raise DonneesInvalidesError(
                "L'arrivée doit être après le départ réel."
            )
        self.arrivee_reelle = instant
        self.statut = StatutMission.LIVREE

    def annuler(self) -> None:
        """Annule une mission qui n'a pas encore commencé."""
        if self.statut is not StatutMission.PLANIFIEE:
            raise DonneesInvalidesError(
                "Seule une mission planifiée peut être annulée."
            )
        self.statut = StatutMission.ANNULEE