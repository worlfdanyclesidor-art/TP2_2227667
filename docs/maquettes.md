# Maquettes de l’application de transport

## Écran principal — Missions de transport

```text
+--------------------------------------------------------------------------+
| TranspoGest              [Commandes] [Missions] [Chauffeurs] [+ Nouveau] |
+--------------------------------------------------------------------------+
| Rechercher : [________________]  Statut : [Tous v]  Date : [Toutes v]    |
+--------------------------------------------------------------------------+
| Mission | Commande | Départ       | Arrivée      | Chauffeur | Camion   |
|---------|----------|--------------|--------------|-----------|----------|
| M-101   | C-204    | Montréal     | Québec       | Alex      | TR-10    |
| M-102   | C-205    | Drummondville| Montréal     | Sam       | TR-12    |
+--------------------------------------------------------------------------+
| [Voir détail] [Modifier] [Annuler la mission]              [Actualiser]  |
+--------------------------------------------------------------------------+
```

## Fenêtre — Créer une commande de transport

```text
+----------------------------------------------------------+
| Nouvelle commande                                        |
| Client :             [Choisir un client              v] |
| Adresse de départ :  [                                  ]|
| Adresse d’arrivée :  [                                  ]|
| Date souhaitée :     [AAAA-MM-JJ                        ]|
| Marchandises :       [Ajouter une marchandise]           |
| Quantité :           [                                  ]|
|                                                          |
|                          [Annuler] [Enregistrer]         |
+----------------------------------------------------------+
```

## Écran — Chauffeurs et camions

```text
+----------------------------------------------------------------+
| Ressources                          [+ Chauffeur] [+ Camion]    |
+----------------------------------------------------------------+
| Chauffeurs                    | Camions                         |
| Nom       | Permis | Disponible| Immatriculation | Capacité kg |
| Alex      | VALIDE | Oui       | TR-10           | 12 000      |
| Sam       | VALIDE | Oui       | TR-12           | 8 000       |
+----------------------------------------------------------------+
```