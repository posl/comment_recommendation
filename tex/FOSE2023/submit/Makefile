FILE_NAME := paper
SUBDIR = section
TEMP_FILES := \
    $(FILE_NAME).aux \
    $(FILE_NAME).bbl \
    $(FILE_NAME).log \
    $(FILE_NAME).blg \
    $(FILE_NAME).brf \
    $(FILE_NAME).dvi \
    $(FILE_NAME).out \
	$(FILE_NAME).fls \
	$(FILE_NAME).fdb_latexmk
SECTION_FILES = \
    $(FILE_NAME).tex
BIBTEX_FILES = references.bib
DEBUG=no
ifneq '$(DEBUG)' 'yes'
LATEX_FLAGS="-interaction=batchmode --file-line-error --synctex=1"
endif
LATEX_FLAG_ENC="-kanji=utf8"
OPEN ?= open
.DELETE_ON_ERROR:
################################################################################
# Main paper building
################################################################################
$(FILE_NAME).pdf: $(SECTION_FILES) $(BIBTEX_FILES)
	platex $(LATEX_FLAGS) $(FILE_NAME)
	pbibtex $(FILE_NAME)
	platex $(LATEX_FLAGS) $(FILE_NAME)
	platex $(LATEX_FLAGS) $(FILE_NAME)
	dvipdfmx $(FILE_NAME)
	rm -f $(TEMP_FILES) $(SUBDIR)/*.aux
.PHONY: clean view
clean:
	rm -f $(TEMP_FILES) $(GEN_FIGURES) $(FILE_NAME).pdf $(SUBDIR)/*.aux
view: $(FILE_NAME).pdf
	$(OPEN) $(FILE_NAME).pdf