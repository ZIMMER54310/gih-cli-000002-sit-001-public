# Procédure GitHub - Acti'Dem

## 1. Créer un nouveau dépôt GitHub

Nom exact :

```text
gih-cli-000002-sit-001-public
```

## 2. Déposer le contenu du ZIP

Après décompression, déposer le contenu du dossier extrait à la racine du nouveau dépôt.

GitHub doit afficher directement :

```text
.github
public
01-FICHE-IDENTITE.py
README.md
PROCEDURE-INSTALLATION-GITHUB.md
DSE-CODIFICATION-OFFICIELLE.md
```

Ne pas déposer le dossier parent complet.

## 3. Commit

Message conseillé :

```text
GIH-CLI-000002-SIT-001-PUBLIC-V1.0.3
```

## 4. Azure ensuite

Créer la ressource Azure Static Web Apps dédiée :

```text
dse-cli-000002-sit-001-public
```

Paramètres Azure :

```text
Repository : gih-cli-000002-sit-001-public
Branch : main
App location : public
Api location : vide
Output location : vide
```

## 5. Domaine plus tard

Domaine cible :

```text
actidem.fr
```

À raccorder uniquement après validation de l'URL Azure.
