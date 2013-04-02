#!/bin/bash
while true; do
    inotifywait -qe modify Hodoscek-PhD-2013.md lualatex-template.pandoc bibliography/doctors-bibliography.bib images/*
    pandoc --highlight-style=kate --chapters --template=lualatex-template.pandoc --biblatex --latex-engine=lualatex --bibliography=bibliography/doctors-bibliography.bib -t latex Hodoscek-PhD-2013.md -o tmp.tex && lualatex --interaction=batchmode tmp && biber -U -u tmp && lualatex --interaction=batchmode tmp ; mv tmp.pdf Hodoscek-PhD-2013.pdf && rm -f tmp.*
done
