from dataclasses import dataclass

from tp2_2227667.domain.exceptions import DonneesInvalidesError


@dataclass
class Client:
    """Représente un client qui commande un transport de marchandises."""

    identifiant: int
    nom: str
    courriel: str
    telephone: str
    adresse: str

    def __post_init__(self) -> None:
        """Valide les informations principales du client."""
        if self.identifiant <= 0:
            raise DonneesInvalidesError(
                "L'identifiant du client doit être positif."
            )
        if not self.nom.strip():
            raise DonneesInvalidesError(
                "Le nom du client ne peut pas être vide."
            )
        if not self.courriel.strip():
            raise DonneesInvalidesError(
                "Le courriel du client ne peut pas être vide."
            )
        if not self.telephone.strip():
            raise DonneesInvalidesError(
                "Le téléphone du client ne peut pas être vide."
            )
        if not self.adresse.strip():
            raise DonneesInvalidesError(
                "L'adresse du client ne peut pas être vide."
            )