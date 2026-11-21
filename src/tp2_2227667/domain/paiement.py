from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from tp2_2227667.domain.exceptions import DonneesInvalidesError


@dataclass
class Paiement:
    """Représente un paiement associé à une commande de transport."""

    identifiant: int
    commande_id: int
    date_paiement: datetime
    montant: Decimal
    mode_paiement: str
    reference: str

    def __post_init__(self) -> None:
        """Valide les principales données du paiement."""
        if self.identifiant <= 0 or self.commande_id <= 0:
            raise DonneesInvalidesError(
                "Les identifiants du paiement et de la commande doivent être positifs."
            )
        if self.montant <= 0:
            raise DonneesInvalidesError(
                "Le montant du paiement doit être strictement positif."
            )
        if not self.mode_paiement.strip():
            raise DonneesInvalidesError(
                "Le mode de paiement ne peut pas être vide."
            )
        if not self.reference.strip():
            raise DonneesInvalidesError(
                "La référence du paiement ne peut pas être vide."
            )