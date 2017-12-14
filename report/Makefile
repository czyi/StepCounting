TEX = acmsmall-sample.tex \
	sample10.tex \
	sample11.tex \
	sample1.tex \
	sample2.tex \
	sample3.tex \
	sample4.tex \
	sample5.tex \
	sample6.tex \
	sample7.tex \
	sample8.tex \
	sample9.tex \


CLS = acmsmall.cls

STY = acmcopyright.sty

PACKAGE = acmsmall

PDF = ${TEX:%.tex=%.pdf} acm-update.pdf

PWD= ${shell pwd}

all:
	pdflatex acl2015
	bibtex acl2015
	pdflatex acl2015

clean:
	$(RM) *.aux *.log  *.blg *.bbl

distclean: clean
	$(RM) $(PDF) acm-update.pdf *.bbl

zip: all clean
	zip $(PACKAGE).zip * -x '*~' -x '*.tgz' -x '*.zip' -x CVS -x 'CVS/*'