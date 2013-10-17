TARGETS = traces.pdf comparison.pdf

all: $(TARGETS)
	@echo > /dev/null

traces.pdf: traces.py data/tinytrace.csv data/fulltrace.csv
	./$< data/tinytrace.csv data/fulltrace.csv

comparison.pdf: comparison.py data/tinylog.csv data/fulllog.csv
	./$< data/tinylog.csv data/fulllog.csv

clean:
	@rm -f $(TARGETS)

.PHONY: clean all
