#
# Makefile used to compile the slides. Handles the file dependencies and all
#   build steps.
#
# Requirements:
# * Make sure you execute from the talk's folder.
#

.PHONY: usage build clean open

usage:
	echo "Targets: build, clean, open"

ROOT = $(shell git rev-parse --show-toplevel)
NAME = $(shell basename "$(shell pwd)")

# all relative to pwd
SLIDES_SRC_FOLDER = $(ROOT)/talks/$(NAME)/src/
SLIDES_OUT_FOLDER = $(ROOT)/build/$(NAME)/
SLIDES_PANDOC_ARGS = --listings --number-sections --pdf-engine=xelatex \
	--include-in-header $(SLIDES_SRC_FOLDER)/header.tex \
	--include-after-body $(SLIDES_SRC_FOLDER)/footer.tex \
	--slide-level 3 --standalone

SLIDES_SRC_FILES_MD = $(shell find $(SLIDES_SRC_FOLDER) -type f -name "*.md" | sort)
SLIDES_SRC_FILES_ALL = $(SLIDES_SRC_FILES_MD) $(SLIDES_SRC_FOLDER)/header.tex $(SLIDES_SRC_FOLDER)/footer.tex
SLIDES_OUT_FILEPATH = $(SLIDES_OUT_FOLDER)/$(NAME)
SLIDES_OUT_TEX_FILEPATH = $(SLIDES_OUT_FILEPATH).tex
SLIDES_OUT_PDF_FILEPATH = $(SLIDES_OUT_FILEPATH).pdf
SLIDES_OUT_HANDOUT_TEX_FILEPATH = $(SLIDES_OUT_FILEPATH)-handout-all.tex
SLIDES_OUT_HANDOUT_PDF_FILEPATH = $(SLIDES_OUT_FILEPATH)-handout-all.pdf
SLIDES_OUT_HANDOUT_JPG_FILEPATH = $(SLIDES_OUT_FILEPATH)-handout-%02d.jpg

clean:
	rm -rf $(SLIDES_OUT_FOLDER)

build: $(SLIDES_SRC_FILES_ALL)
	mkdir -p $(SLIDES_OUT_FOLDER)
	pandoc -t beamer -o $(SLIDES_OUT_TEX_FILEPATH) $(SLIDES_PANDOC_ARGS) -- $(SLIDES_SRC_FILES_MD)
	TEXINPUTS="abeamer-theme-metropolis/:" xelatex -output-directory=$(SLIDES_OUT_FOLDER) $(SLIDES_OUT_TEX_FILEPATH)
	cd $(SLIDES_OUT_FOLDER) && BIBINPUTS=$(SLIDES_SRC_FOLDER) bibtex $(NAME).aux
	TEXINPUTS="abeamer-theme-metropolis/:" xelatex -output-directory=$(SLIDES_OUT_FOLDER) $(SLIDES_OUT_TEX_FILEPATH)
	TEXINPUTS="abeamer-theme-metropolis/:" xelatex -output-directory=$(SLIDES_OUT_FOLDER) $(SLIDES_OUT_TEX_FILEPATH)
	ls $(SLIDES_OUT_FILEPATH).* | grep -v -E "pdf|tex" | xargs rm -f
	echo "Slides built to $(SLIDES_OUT_PDF_FILEPATH)"

build-handout:
	mkdir -p $(SLIDES_OUT_FOLDER)
	pandoc -t beamer -o $(SLIDES_OUT_HANDOUT_TEX_FILEPATH) $(SLIDES_PANDOC_ARGS) -V handout -- $(SLIDES_SRC_FILES_MD)
	TEXINPUTS="abeamer-theme-metropolis/:" xelatex -output-directory=$(SLIDES_OUT_FOLDER) $(SLIDES_OUT_HANDOUT_TEX_FILEPATH)
	cd $(SLIDES_OUT_FOLDER) && BIBINPUTS=$(SLIDES_SRC_FOLDER) bibtex $(NAME)-handout-all.aux
	TEXINPUTS="abeamer-theme-metropolis/:" xelatex -output-directory=$(SLIDES_OUT_FOLDER) $(SLIDES_OUT_HANDOUT_TEX_FILEPATH)
	TEXINPUTS="abeamer-theme-metropolis/:" xelatex -output-directory=$(SLIDES_OUT_FOLDER) $(SLIDES_OUT_HANDOUT_TEX_FILEPATH)
	ls $(SLIDES_OUT_FILEPATH)-* | grep -v -E "pdf|tex" | xargs rm -f
	convert -density 300 -quality 100 $(SLIDES_OUT_HANDOUT_PDF_FILEPATH) $(SLIDES_OUT_HANDOUT_JPG_FILEPATH)

open:
	xdg-open $(SLIDES_OUT_PDF_FILEPATH) &
