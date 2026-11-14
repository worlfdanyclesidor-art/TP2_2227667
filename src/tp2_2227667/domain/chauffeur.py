from dataclasses import dataclass


@dataclass
class Chauffeur:
    """Représente un chauffeur de l'entreprise de transport."""

    identifiant: int
    nom: str
    prenom: str
    numero_permis: str
    disponible: bool = True