# Makefile

# Usage: make target1 target2 ...

#------------------------------------------------------------------------------

# GNU C/C++ compiler and linker:
LINK = g++

# Preprocessor and compiler flags (turn on warning, optimization, and debugging):
# CPPFLAGS = <preprocessor flags go here>

CFLAGS = -Wall -O -g
CXXFLAGS = $(CFLAGS)

#------------------------------------------------------------------------------
# Targets

all: cns_channel

#------------------------------------------------------------------------------

cns_channel: main.o video.o episode.o spot.o show.o
	$(LINK) -o $@ $^

#------------------------------------------------------------------------------

clean:
	rm -f *.o *~ core

cleanall:
	rm -f *.o *~ core cns_channel
