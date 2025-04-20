# Base de Données CICDDoS2019

La base de données **CICDDoS2019** (Canadian Institute for Cybersecurity - Distributed Denial of Service 2019) est un ensemble de données conçu pour soutenir la recherche et le développement en cybersécurité, avec un accent particulier sur les attaques par **déni de service distribué (DDoS)**.

Elle a été élaborée par l’Institut canadien de cybersécurité (Canadian Institute for Cybersecurity, CIC) afin d’offrir une ressource complète aux chercheurs, universitaires et professionnels de la sécurité informatique.

🔗 **Description complète de la base de données :**  
[https://www.unb.ca/cic/datasets/ddos-2019.html](https://www.unb.ca/cic/datasets/ddos-2019.html)

---

## 📁 Structure des fichiers

Les données sont organisées en plusieurs fichiers, chacun représentant un type spécifique d’attaque DDoS. Les attaques ont été dirigées vers deux adresses IP distinctes pendant la période analysée. Le tableau ci-dessous présente les attaques par jour, IP cible et horaire :

### 📊 Tableau des attaques

#### 03-11-2018 (192.168.50.4)
| Type d’attaque | Heure       |
|----------------|-------------|
| PortMap        | 09:43-09:51 |
| NetBIOS        | 10:00-10:09 |
| LDAP           | 10:21-10:30 |
| MSSQL          | 10:33-10:42 |
| UDP            | 10:53-11:03 |
| UDP-Lag        | 11:14-11:24 |
| SYN            | 11:28-17:35 |

#### 01-12-2018 (192.168.50.1)
| Type d’attaque | Heure       |
|----------------|-------------|
| NTP            | 10:35-10:45 |
| DNS            | 10:52-11:05 |
| LDAP           | 11:22-11:32 |
| MSSQL          | 11:36-11:45 |
| NetBIOS        | 11:50-12:00 |
| SNMP           | 12:12-12:23 |
| SSDP           | 12:27-12:37 |
| UDP            | 12:45-13:09 |
| UDP-Lag        | 13:11-13:15 |
| SYN            | 13:29-13:34 |
| TFTP           | 13:35-17:15 |

---

## 🧩 Applications

La base de données CICDDoS2019 est essentielle pour progresser dans la compréhension et la protection contre les attaques DDoS, contribuant à renforcer la sécurité des infrastructures réseau à l’échelle mondiale.

### Usages principaux :

- **Recherche scientifique** : analyse de nouvelles méthodes de détection et de mitigation des attaques DDoS.
- **Développement d’outils de sécurité** : création et optimisation de systèmes de détection d’intrusion (IDS) et de prévention d’intrusion (IPS).
- **Benchmarking** : comparaison de l’efficacité des solutions de sécurité contre divers types d’attaques.

---

## ⚙️ Prétraitement des données

### 1. Sélection des données

#### **Entraînement et validation :**
Les données du **03-11-2018 (IP : 192.168.50.4)** ont été utilisées pour l’entraînement et la validation du modèle. Elles incluent les attaques suivantes :
- PortMap, NetBIOS, LDAP, MSSQL, UDP, UDP-Lag, SYN.

#### **Test pour la généralisation :**
Les données du **01-12-2018 (IP : 192.168.50.1)** ont été utilisées séparément comme ensemble de test afin d’évaluer la capacité de généralisation du modèle pré-entraîné :
- NTP, DNS, LDAP, MSSQL, NetBIOS, SNMP, SSDP, UDP, UDP-Lag, SYN, TFTP.

---

## ✅ Conclusion

La base de données CICDDoS2019 fournit une ressource précieuse pour le développement de modèles robustes de détection d’attaques DDoS et pour l’évaluation comparative des outils de cybersécurité.

