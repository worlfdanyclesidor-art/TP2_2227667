from dataclasses import dataclass
from decimal import Decimal

from tp2_2227667.domain.exceptions import DonneesInvalidesError


@dataclass
class Marchandise:
    """Représente un type de marchandise transportable."""

    identifiant: int
    nom: str
    poids_unitaire_kg: Decimal
    description: str = ""

    def __post_init__(self) -> None:
        """Valide les données de la marchandise après son initialisation."""
        if self.identifiant <= 0:
            raise DonneesInvalidesError(
                "L'identifiant de la marchandise doit être positif."
            )
        if not self.nom.strip():
            raise DonneesInvalidesError(
                "Le nom de la marchandise ne peut pas être vide."
            )
        if self.poids_unitaire_kg <= 0:
            raise DonneesInvalidesError(
                "Le poids unitaire doit être positif."
            )