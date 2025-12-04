# Module Gestion École

Module Odoo 17 pour la gestion d'une école avec extension du module Contact natif.

## 🎯 Fonctionnalités

- **Responsables Pédagogiques (RP)** : Gestion des coordinateurs de formations
- **Formations** : Création et suivi des programmes de formation
- **Étudiants** : Gestion des étudiants avec vues optimisées
- **Alumni** : Suivi des anciens étudiants
- **Intervenants** : Gestion des formateurs et intervenants externes

## 📋 Architecture

### Extension de `res.partner`
Le module étend le modèle natif Odoo `res.partner` pour ajouter :
- `type_profil` : Selection (etudiant, alumni, intervenant, salarie, rp)
- `is_rp` : Boolean pour identifier les Responsables Pédagogiques
- `is_alumni` : Boolean pour les anciens étudiants
- `is_intervenant` : Boolean pour les formateurs
- `formation_id` : Many2one vers school.formation
- `poste` : Char pour le poste occupé

### Modèle `school.formation`
- `type_formation` : Nom de la formation
- `rp_id` : Many2one vers res.partner (RP uniquement)
- `etudiant_ids` : One2many vers les étudiants
- `etudiant_count` : Compteur calculé

## 🎨 Vues séparées

Chaque type de personne dispose de vues optimisées :
- **Étudiants** : Vue avec formation obligatoire
- **Alumni** : Vue avec parcours professionnel
- **Intervenants** : Vue avec compétences
- **RP** : Vue avec formations gérées
- **Toutes les Personnes** : Vue générique

## 📦 Installation

1. Placer le module dans le dossier addons d'Odoo
2. Redémarrer Odoo : `sudo systemctl restart odoo`
3. Mettre à jour la liste des applications
4. Installer "Gestion École"

## 🔗 Dépendances

- `base` (module natif Odoo)

## 👨‍💻 Auteur

MoonDev - 2025
