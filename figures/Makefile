TARGETS = traces.pdf

all: $(TARGETS)
	@echo > /dev/null

traces.pdf: traces.py traces/tinytrace.csv traces/fulltrace.csv
	./$< traces/tinytrace.csv traces/fulltrace.csv

clean:
	@rm -f $(TARGETS)

.PHONY: clean all
