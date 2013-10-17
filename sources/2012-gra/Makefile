# 10 Jul 2010 : GWA : Add subdirs here as needed. They will be built into the
# 						  complete document in order. Probably best to have each
# 						  correspond to a chapter in the thesis, but that's not
# 						  strictly required.

START = xxxnote
END = missing
CLASS = $(PYTEX)/cls/googleproposal.cls

#all: proposal abstract.txt
all: proposal complete.pdf abstract.txt

figures:
	@cd figures ; make

complete.pdf: proposal.pdf ./resumes/challen/challen.pdf
	@pdfjoin proposal.pdf ./resumes/challen/challen.pdf -o complete.pdf

abstract.txt: abstract.tex $(PYTEX)/bin/clean $(PYTEX)/bin/lib.py
	@$(PYTEX)/bin/clean abstract.tex abstract.txt

# 16 Nov 2010 : GWA : Add other cleaning rules here.

clean: rulesclean
	@/bin/rm -f complete.pdf abstract.txt

include $(PYTEX)/make/Makerules
