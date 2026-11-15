from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from enum import Enum

from tp2_2227667.domain.exceptions import DonneesInvalidesError
from tp2_2227667.domain.marchandise import Marchandise


class StatutCommande(Enum):
    """États possibles d'une commande de transport."""

    EN_ATTENTE = "en_attente"
    CONFIRMEE = "confirmee"
    TERMINEE = "terminee"
    ANNULEE = "annulee"


@dataclass(frozen=True)
class LigneCommande:
    """Associe une marchandise à une quantité dans une commande."""

    marchandise: Marchandise
    quantite: int

    def __post_init__(self) -> None:
        """Vérifie que la quantité de marchandises est positive."""
        if self.quantite <= 0:
            raise DonneesInvalidesError(
                "La quantité doit être strictement positive."
            )

    def calculer_poids(self) -> Decimal:
        """Calcule le poids total de cette ligne de commande."""
        return self.marchandise.poids_unitaire_kg * self.quantite


@dataclass
class CommandeTransport:
    """Représente une commande de transport de marchandises."""

    identifiant: int
    client: str
    adresse_depart: str
    adresse_arrivee: str
    date_livraison_souhaitee: date
    montant_total: Decimal
    date_commande: datetime = field(default_factory=datetime.now)
    statut: StatutCommande = StatutCommande.EN_ATTENTE
    lignes: list[LigneCommande] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Valide les données principales de la commande."""
        if self.identifiant <= 0:
            raise DonneesInvalidesError(
                "L'identifiant de la commande doit être positif."
            )
        if not self.client.strip():
            raise DonneesInvalidesError(
                "Le client ne peut pas être vide."
            )
        if not self.adresse_depart.strip():
            raise DonneesInvalidesError(
                "L'adresse de départ ne peut pas être vide."
            )
        if not self.adresse_arrivee.strip():
            raise DonneesInvalidesError(
                "L'adresse d'arrivée ne peut pas être vide."
            )
        if self.montant_total < 0:
            raise DonneesInvalidesError(
                "Le montant total ne peut pas être négatif."
            )

    def ajouter_marchandise(
        self,
        marchandise: Marchandise,
        quantite: int,
    ) -> None:
        """Ajoute une marchandise à la commande avec sa quantité."""
        if any(
                ligne_existante.marchandise.identifiant == marchandise.identifiant
                for ligne_existante in self.lignes
        ):
            raise DonneesInvalidesError(
                "Cette marchandise est déjà présente dans la commande."
            )
        ligne = LigneCommande(marchandise=marchandise, quantite=quantite)
        self.lignes.append(ligne)

    def calculer_poids_total(self) -> Decimal:
        """Calcule le poids de toutes les marchandises de la commande."""
        return sum(
            (ligne.calculer_poids() for ligne in self.lignes),
            start=Decimal("0"),
        )