from dataclasses import dataclass
from decimal import Decimal

from tp2_2227667.domain.exceptions import DonneesInvalidesError


@dataclass
class Camion:
    """Représente un camion utilisé pour le transport de marchandises."""

    identifiant: int
    immatriculation: str
    capacite_kg: Decimal
    disponible: bool = True

    def __post_init__(self) -> None:
        """Valide les données du camion après son initialisation."""
        if self.identifiant <= 0:
            raise DonneesInvalidesError(
                "L'identifiant du camion doit être positif."
            )
        if not self.immatriculation.strip():
            raise DonneesInvalidesError(
                "L'immatriculation ne peut pas être vide."
            )
        if self.capacite_kg <= 0:
            raise DonneesInvalidesError(
                "La capacité du camion doit être positive."
            )