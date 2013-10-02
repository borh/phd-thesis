#!/bin/bash
while true; do
    inotifywait -qe modify Hodoscek-PhD-2013.md lualatex-template.pandoc bibliography/doctors-bibliography.bib images/*
    pandoc --no-wrap --highlight-style=kate --chapters --template=lualatex-template.pandoc --biblatex --latex-engine=lualatex \
           -f markdown+grid_tables+auto_identifiers+implicit_header_references+example_lists+intraword_underscores+superscript+subscript \
           --smart \
           --bibliography=bibliography/doctors-bibliography.bib -t latex+grid_tables+auto_identifiers+implicit_header_references+example_lists+intraword_underscores+superscript+subscript Hodoscek-PhD-2013.md -o tmp-pandoc.tex && \
           cat tmp-pandoc.tex | ./fix-tables.py > tmp.tex && \
           lualatex --shell-escape --interaction=batchmode tmp && biber -U -u tmp ; mv tmp.pdf Hodoscek-PhD-2013.pdf && cp Hodoscek-PhD-2013.pdf ~/Dropbox/My\ Papers/ #&& rm -f tmp.*
           # lualatex --interaction=batchmode tmp ; \
done
