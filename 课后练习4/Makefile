.PHONY: all clean list

all: paper.pdf

list:
	git ls-files

paper.pdf: paper.tex
	pdflatex paper.tex

clean:
	rm -f paper.pdf paper.aux paper.log
