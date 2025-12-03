# Architecture des Modules Odoo - Gestion École

## 📦 Modules disponibles

### 1️⃣ gestion_ecole (BASE)
**Gestion des formations, RP et étudiants**

**Modèles:**
- `res.partner` (extension) - Responsables Pédagogiques
- `school.formation` - Formations
- `school.personne` - Étudiants, Alumni, Intervenants, Salariés

**Dépendances:** `base`

---

### 2️⃣ groupe_entreprise (à renommer en gestion_entreprise)
**Gestion des groupes d'entreprises et entreprises**

**Modèles:**
- `entreprise.groupe` - Groupes d'entreprises
- `entreprise.entreprise` - Entreprises

**Dépendances:** `base`, `gestion_ecole`

---

### 3️⃣ gestion_contrat
**Gestion des contrats d'alternance et de stage**

**Modèles:**
- `contrat.contrat` - Contrats (alternance/stage)
- `school.personne` (extension) - Ajout des relations vers contrats

**Dépendances:** `base`, `gestion_ecole`, `groupe_entreprise`

---

## 🔄 Relations entre les tables

```
RP (res.partner)
  └─> FORMATION (school.formation)
        └─> PERSONNE (school.personne) [type: etudiant]

GROUPE (entreprise.groupe)
  └─> ENTREPRISE (entreprise.entreprise)
        └─> PERSONNE (school.personne) [type: salarie]

CONTRAT (contrat.contrat)
  ├─> PERSONNE [étudiant]
  ├─> ENTREPRISE
  └─> PERSONNE [tuteur/salarié]
```

---

## 📋 Ordre d'installation OBLIGATOIRE

⚠️ **IMPORTANT:** Installer dans cet ordre pour éviter les erreurs de dépendances

1. **gestion_ecole**
2. **groupe_entreprise** (renommer le dossier en `gestion_entreprise` d'abord)
3. **gestion_contrat**

---

## ⚙️ Installation

### Étape 1: Préparation
```bash
# Renommer le module groupe_entreprise
cd /chemin/vers/addons
mv groupe_entreprise gestion_entreprise
```

### Étape 2: Installation dans Odoo
1. Redémarrer Odoo
2. Activer le mode développeur
3. Applications → Mettre à jour la liste des applications
4. Installer **gestion_ecole**
5. Installer **gestion_entreprise** (anciennement groupe_entreprise)
6. Installer **gestion_contrat**

---

## 🛠️ Corrections appliquées

### ✅ Problèmes résolus:
- Dépendances circulaires entre modules
- Relations `One2many` déclarées dans le bon module
- Ajout de `ondelete='set null'` pour les clés étrangères
- Utilisation de `attrs` au lieu de `invisible` (Odoo 17)
- Vues héritées correctement structurées

### ⚠️ Points d'attention:
- Le champ `entreprise_id` dans `school.personne` référence un modèle du module `groupe_entreprise`
- Les champs `contrat_etudiant_ids` et `contrat_tuteur_ids` sont ajoutés par héritage dans `gestion_contrat`
- Ne pas installer les modules dans le mauvais ordre

---

## 📊 Structure de la base de données

### Tables principales:
- `res_partner` (Odoo standard + is_rp)
- `school_formation`
- `school_personne`
- `entreprise_groupe`
- `entreprise_entreprise`
- `contrat_contrat`

### Clés étrangères:
- `school_formation.rp_id` → `res_partner.id`
- `school_personne.formation_id` → `school_formation.id`
- `school_personne.entreprise_id` → `entreprise_entreprise.id`
- `entreprise_entreprise.groupe_id` → `entreprise_groupe.id`
- `contrat_contrat.personne_etudiant_id` → `school_personne.id`
- `contrat_contrat.personne_tuteur_id` → `school_personne.id`
- `contrat_contrat.entreprise_id` → `entreprise_entreprise.id`

---

## 🐛 Dépannage

### Erreur: "KeyError: 'personne_etudiant_id'"
**Cause:** Module gestion_contrat installé avant gestion_ecole
**Solution:** Désinstaller gestion_contrat, puis réinstaller dans le bon ordre

### Erreur: "Model not found: entreprise.entreprise"
**Cause:** Module groupe_entreprise/gestion_entreprise non installé
**Solution:** Installer gestion_entreprise avant gestion_contrat

### Erreur: "column does not exist"
**Cause:** Module non mis à jour après modification
**Solution:** Apps → Rechercher le module → Mettre à jour

---

## 📝 Version
- **Odoo:** 17.0
- **Auteur:** MoonDev
- **Date:** Décembre 2025
