# Metal Gear Album Panini

## Structure

    metal-gear-album/
    index.html                   <- Ouvrir dans le navigateur
    covers/                      <- Images des couvertures
        001.jpg  Metal Gear (1987)
        002.jpg  Metal Gear 2: Solid Snake (1990)
        003.jpg  Metal Gear Solid (1998)
        004.jpg  Metal Gear Solid 2: Sons of Liberty (2001)
        005.jpg  MGS: The Twin Snakes (2004)
        006.jpg  MGS4: Guns of the Patriots (2008)
        007.jpg  Metal Gear Solid 3: Snake Eater (2004)
        008.jpg  MGS: Portable Ops (2006)
        009.jpg  MGS: Peace Walker (2010)
        010.jpg  MGSV: Ground Zeroes (2014)
        011.jpg  MGSV: The Phantom Pain (2015)
        012.jpg  Metal Gear Rising: Revengeance (2013)
        013.jpg  Metal Gear Survive (2018)

## Ajouter les covers

1. Trouvez la cover du jeu (JPG, ratio 2/3, ex: 300x450px)
2. Renommez-la avec l ID correspondant (ex: 003.jpg pour MGS1)
3. Remplacez le fichier placeholder dans covers/
4. Rechargez index.html : la cover s affiche automatiquement

## GitHub Pages

1. Pushez ce dossier sur GitHub
2. Repo Settings -> Pages -> Source: main, dossier /root
3. Votre album sera sur https://[pseudo].github.io/[repo]/

## Notes

- Les images dans covers/ se chargent automatiquement au demarrage
- En mode Admin (bouton ADM) vous pouvez uploader une image par jeu
- Les images uploadees via ADM ont priorite sur covers/
- Ratio recommande pour les covers : 2/3 (portrait)
