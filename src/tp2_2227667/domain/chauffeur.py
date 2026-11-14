from dataclasses import dataclass


@dataclass
class Chauffeur:
    """Représente un chauffeur de l'entreprise de transport."""

    identifiant: int
    nom: str
    prenom: str
    numero_permis: str
    disponible: bool = True

    def __post_init__(self) -> None:
        """Valide les champs du chauffeur après son initialisation."""
        if self.identifiant <= 0:
            raise ValueError("L'identifiant doit être positif.")
        if not self.nom.strip():
            raise ValueError("Le nom ne peut pas être vide.")
        if not self.prenom.strip():
            raise ValueError("Le prénom ne peut pas être vide.")
        if not self.numero_permis.strip():
            raise ValueError("Le numéro de permis ne peut pas être vide.")
