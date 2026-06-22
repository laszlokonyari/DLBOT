# DLBOT

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![](https://img.shields.io/badge/Discord.py-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![](https://img.shields.io/badge/FFmpeg-007800?style=for-the-badge&logo=ffmpeg&logoColor=white)
![](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)

---
Docker alapú Discord bot audió tartalmak letöltésére, konvertálására és továbbítására.

---

## Funkciók

* Docker architektúra: Előre konfigurált FFmpeg és Node.js környezet.
* Függőségmentes futtatás: Nem igényli szoftverek telepítését a gazdagépen.
* SoundCloud támogatás: Audió kinyerése SoundCloud hivatkozásokból.
* Discord slash parancsok kezelése.

---

## YouTube korlátozások

Adatközponti IP-címek (pl. DigitalOcean, AWS, Hetzner) használata esetén a YouTube szerverei blokkolják a kéréseket (Sign in to confirm you’re not a bot / Error 152-18). A forráskód tartalmazza az aktuális megkerülési kísérleteket, de a stabil működés csak SoundCloud hivatkozásokkal garantált.

---

## Előfeltételek

* Docker
* Docker Compose

---

## Telepítés és indítás

1. Repo klónozása:
`git clone https://github.com/laszlokonyari/DLBOT.git && cd DLBOT`

2. Környezeti változók:
Hozz létre egy `.env` fájlt a gyökérmappában az alábbi tartalommal:
DISCORD_TOKEN=botod_tokenje

3. App indítása:
docker compose up -d --build

4. Logok megtekintése:
docker compose logs -f

---

## Frissítés

Módosítások alkalmazása a távoli szerveren:

git pull
docker compose up -d --build

---

## Licenc

Nyílt forráskódú szoftver.