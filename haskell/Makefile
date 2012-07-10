SOURCE = square1.hs
EXE = solve
ARTIFACTS = $(wildcard $(EXE)) $(wildcard *.hi) $(wildcard *.o) $(wildcard *.prof)

all: $(EXE)

clean:
	rm -f $(ARTIFACTS)

$(EXE): $(SOURCE)
	ghc -o $(@) --make $(^)

profiled: $(SOURCE)
	ghc -prof -auto-all -rtsopts -o $(EXE) $(^)
