# TP2_2227667

Application de bureau pour planifier le transport de marchandises. Elle permettra de gérer les commandes, les chauffeurs et les camions, puis de suivre les missions de transport.

## Fonctionnalités prévues

- Gérer les chauffeurs et les camions.
- Créer des commandes de transport avec les adresses de départ et d’arrivée.
- Ajouter des marchandises et leurs quantités à une commande.
- Planifier une mission avec un chauffeur et un camion.
- Vérifier la disponibilité du chauffeur et du camion pendant la période prévue.
- Suivre l’état des commandes et des missions.

## Architecture prévue

- `domain` : contient les classes métier et les règles de gestion.
- `application` : coordonne les opérations de planification.
- `infrastructure` : gérera la sauvegarde des données.
- `presentation` : contiendra l’interface graphique.
- `domain/mixins` : contiendra les comportements partagés, comme le suivi des dates.