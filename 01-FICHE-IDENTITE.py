# -*- coding: utf-8 -*-
"""
DEMAINSITE ECOSYSTEME - FICHE GITHUB OFFICIELLE
Objet : dépôt GitHub dédié site public Acti'Dem
Client : CLI-000002 - Acti'Dem
Site : CLI-000002-SIT-001 - Site public principal
GitHub : GIH-CLI-000002-SIT-001-PUBLIC
Azure : DSE-CLI-000002-SIT-001-PUBLIC
Domaine : actidem.fr
Propriétaire : Pascal ZIMMER
Assistance : PascARA
Organisation : DemainSite
Date : 2026-08-13
"""

PROJET = {
    "schema_version": "DSE-GIH-CLIENT-SITE-V1.0.3",
    "procedure_officielle": "1 client = 1 code client unique + 1 ou plusieurs sites + 1 depot GitHub dedie par site + 1 Azure Static Web App dediee par site + 1 structure SharePoint dediee",
    "id_unique_permanent": "GIH-CLI-000002-SIT-001-PUBLIC",
    "point_reprise_officiel": "GIH-CLI-000002-SIT-001-PUBLIC-V1.0.3",
    "proprietaire": {
        "nom": "Pascal ZIMMER",
        "assistant_ia": "PascARA",
        "organisation": "DemainSite",
        "signature_obligatoire": "Pascal ZIMMER - PascARA - DemainSite"
    },
    "client": {
        "code_client": "CLI-000002",
        "nom_officiel": "Acti'Dem",
        "statut": "CLIENT_ACTIF"
    },
    "site": {
        "code_site": "CLI-000002-SIT-001",
        "type_site": "PUBLIC",
        "nom_site": "Site public principal Acti'Dem",
        "domaine_principal": "actidem.fr",
        "statut": "CONSTRUCTION"
    },
    "github": {
        "code_github": "GIH-CLI-000002-SIT-001-PUBLIC",
        "nom_depot_officiel": "gih-cli-000002-sit-001-public",
        "branche": "main",
        "app_location": "public",
        "workflow": ".github/workflows/azure-static-web-apps.yml",
        "secret_deploiement": "AZURE_STATIC_WEB_APPS_API_TOKEN"
    },
    "azure": {
        "code_azure": "DSE-CLI-000002-SIT-001-PUBLIC",
        "nom_ressource": "dse-cli-000002-sit-001-public",
        "type": "Azure Static Web Apps",
        "region": "West Europe",
        "plan": "Free"
    },
    "sharepoint": {
        "source_officielle": True,
        "structure_dediee_client": "CLI-000002",
        "structure_dediee_site": "CLI-000002-SIT-001",
        "sync_media": True,
        "suppression_proprietaire": "MISE_INACTIVE_UNIQUEMENT",
        "suppression_definitive": "SUPER_ADMIN_UNIQUEMENT"
    },
    "codification_objets": {
        "client": "CLI-000002",
        "site": "CLI-000002-SIT-001",
        "github": "GIH-CLI-000002-SIT-001-PUBLIC",
        "azure": "DSE-CLI-000002-SIT-001-PUBLIC",
        "domaines": {
            "principal": "CLI-000002-SIT-001-DOM-001",
            "alias": "CLI-000002-SIT-001-DOM-002"
        },
        "medias": {
            "musique": "CLI-000002-MUS-000001",
            "photo": "CLI-000002-PHO-000001",
            "video": "CLI-000002-VID-000001",
            "banderole": "CLI-000002-BAN-000001",
            "document": "CLI-000002-DOC-000001"
        },
        "evenement": "CLI-000002-EVT-000001",
        "projet": "CLI-000002-PROJ-000001",
        "reseau_social": "CLI-000002-SOC-000001",
        "utilisateur": "CLI-000002-USR-000001"
    },
    "regles_obligatoires": [
        "Le dépôt GitHub doit être dédié au site et nommé avec le code GIH + CLI + SIT + PUBLIC.",
        "Ne pas ranger le site client dans ecosysteme-demainsite.",
        "Un client peut avoir plusieurs sites : CLI-000002-SIT-001, CLI-000002-SIT-002, etc.",
        "Un site peut avoir plusieurs domaines : CLI-000002-SIT-001-DOM-001, DOM-002, etc.",
        "Chaque média possède un code typé : MUS, PHO, VID, BAN, DOC.",
        "Tous les codes sont permanents, non modifiables, non recyclés et servent de référence dans SharePoint.",
        "SharePoint reste la source officielle.",
        "Un propriétaire peut rendre un média inactif mais ne peut pas le supprimer définitivement."
    ]
}

POINT_REPRISE = PROJET["point_reprise_officiel"]

if __name__ == "__main__":
    import json
    print(json.dumps(PROJET, ensure_ascii=False, indent=4))
