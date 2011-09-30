all: solve

clean:
	rm solve *.hi *.o *.prof

solve: square1.hs
	ghc -o $(@) --make square1.hs
