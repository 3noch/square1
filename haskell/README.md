Haskell
=======


Building
--------

To build the [Haskell](http://haskell.org) implementation:

    $ make

To run, for example:

    $ ./solve "[(1,1),(10,30)]"


Profiling
---------

To compile the Haskell implementation with profiling enabled, do this:

    $ make profiled

Then run the program like this:

    $ ./solve ... +RTS -p


The Killer Problem
------------------

The killer problem is this:

    $ ./solve "[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(10,30),(20,70),(30,40),(40,20),(50,50),(60,60),(70,80),(80,10)]"
