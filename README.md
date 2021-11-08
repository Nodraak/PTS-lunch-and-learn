# README.md

*Repo hosting my slides of PTS's Wednesdays *Lunch and Learn* talks. View the slides [here](../../tree/build/build/).*


## Talk Planning

**Planned**

| Date       | Event(s)         | Subject                                                   |
|------------|------------------|-----------------------------------------------------------|
| 2021-11-03 | Crew-3 (31 oct)  | ISS crew rotation (Matthias Maurer), ISS Launch Windows   |
| 2021-11-17 | DART (24 nov)    | HERA, mech orb, asteroid destruction                      |
| 2021-12-08 | JWST (18 dec)    | Lagrange points                                           |
| 2021-12-15 | JWST (18 dec)    | Temperature control, sensors (IR), ...                    |
| 2022-01-05 | PLD, Themis      | Propulsion, rocket design convergence (Falcon 9 type)     |
| 2022-02-02 |  |  |
| 2022-03-02 | A5 Heinrich Hertz | ? |
| 2022-04-06 | Galileo, Oneweb, Peregrine | GPS, com constellation, going to / landing on the Moon |
| 2022-05-04 |  |  |
| 2022-06-01 |  |  |
| 2022-07-06 | Isar demo flight, RFA One |  |
| 2022-08-03 | Psyche, JUICE | Asteroids, mech orb, stars formation and life (Jupiter) |
| 2022-09-07 | Exomars | Landing on Mars |
| 2022-10-xx | Ariane 6 | Trajectory optimisation, launcher design |
| ? | Space Rider | |

**Anniversaries**

* Bepicolombo
    * Fly by
* Solar orbiter
    * TBD events

**Topics**

* History of spaceflight
* Orbital mechanics
    * ASTRIS: https://kb.pts.space/display/SAWS/Mission+Profiles
    * Go to / land on the Moon
    * Propulsion (dv)
    * Halo orbits around the Moon -> LOPG
    * Lagrange points (done via JWST?)
* GNC/AOCS
    * GNC
    * AOCS sensors/actuators
* Human spaceflight
    * Recycling and living in closed cycle (ISS)
    * Spacesuits: pressure vs oxygen, external dust (Apollo), temperature control (Luca Parmitano's water)
* Propulsion (engine)
    * High level comparaison
    * Detailled liquid -> A5
    * Detailled solid -> Vega
    * Detailled electric
    * Detaileld methane -> Themis, Starship, ...
* Launch chronology (prelaunch, ascent)
* ISS rendez vous and docking


## Repo Usage

**Quickstart**

```bash
pip3 install -r tools/requirements.txt
apt install texlive-full
invoke build 00-1970-01-01-template
# look into build/00-1970-01-01-template/
```

**Sources**

Theme source: https://github.com/matze/mtheme

**Manual Install**

Minimal set (debian):

* lmodern
* pandoc >=2.0 https://github.com/jgm/pandoc/releases
* texlive
* texlive-luatex
* texlive-xetex

Minimal set (centos):

* texlive
* texlive-babel-french
* texlive-beamertheme-metropolis
* texlive-framed
* texlive-mathspec
* texlive-mdframed
* texlive-titlesec
* texlive-tocloft
* texlive-ulem

Optional packages:

* fonts-lato
* fonts-texgyre
* ghostscript
* gsfonts
* tex-gyre
* texlive-extra-utils
* texlive-font-utils
* texlive-generic-extra
* texlive-generic-recommended
* texlive-pictures
* texlive-pstricks
