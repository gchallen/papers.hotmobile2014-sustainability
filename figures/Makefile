TARGETS = traces.pdf

all: $(TARGETS)
	@echo > /dev/null

traces.pdf: traces.py tinytrace.csv fulltrace.csv
	./$< tinytrace.csv fulltrace.csv

clean:
	@rm -f $(TARGETS)

.PHONY: clean all
