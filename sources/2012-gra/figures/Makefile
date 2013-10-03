TARGETS = applicationsupporters.tex \
					infrastructuresupporters.tex \
					networkingsupporters.tex \
					supporttable.tex \
					systemssupporters.tex

all: $(TARGETS)
	@echo > /dev/null

applicationsupporters.tex: gensupportlists.py PhoneLabSupporters.csv
	./$< PhoneLabSupporters.csv
infrastructuresupporters.tex: gensupportlists.py PhoneLabSupporters.csv
	./$< PhoneLabSupporters.csv
networkingsupporters.tex: gensupportlists.py PhoneLabSupporters.csv
	./$< PhoneLabSupporters.csv
systemssupporters.tex: gensupportlists.py PhoneLabSupporters.csv
	./$< PhoneLabSupporters.csv

supporttable.tex: gensupporttable.py PhoneLabSupporters.csv
	./$< PhoneLabSupporters.csv

clean:
	@rm -f $(TARGETS)

.PHONY: clean all
