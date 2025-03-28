# SSH Remote Connection using Paramiko

## Description
Ce projet utilise la bibliothèque **Paramiko** pour permettre une **connexion SSH à distance** entre un client et un serveur. Paramiko est une bibliothèque Python qui permet de gérer des connexions SSH (Secure Shell) de manière sécurisée, en fournissant une interface pour établir des connexions SSH, exécuter des commandes à distance et transférer des fichiers.

Ce projet permet de se connecter à un serveur distant, d'exécuter des commandes à distance et d'interagir avec le système à distance via SSH, tout cela en utilisant des scripts Python.

## Fonctionnalités
- **Connexion SSH à un serveur distant** : Utilisez des informations d'identification (nom d'utilisateur, mot de passe, clé privée) pour vous connecter à un serveur distant.
- **Exécution de commandes à distance** : Exécutez des commandes directement sur le serveur distant via SSH.
- **Transfert de fichiers** : Transférez des fichiers entre votre machine locale et le serveur distant via SCP (Secure Copy Protocol).
- **Gestion des sessions SSH** : Gérez facilement les sessions SSH et les erreurs.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé la bibliothèque Paramiko. Si ce n'est pas déjà fait, vous pouvez l'installer avec pip :

```bash
pip install paramiko
