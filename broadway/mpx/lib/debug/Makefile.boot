##
# An odd sort of Makefile that generates the Makefile required to build the
# Python extension modules (shared libraries).  It ensures that the Makefile
# is generated from the source controlled input files (Makefile.pre.in and
# Setup.in, and not by modified target files (Makefile.pre, Makefile, and
# Setup).  It also checks the dependencies of the source files, which the
# standard Makefile doesn't seem to do.
#
# Requires PYTHON and EVAL command line variables (use ./compile)

all: valid

_MAKETARGETS=Makefile Makefile.pre Setup
_MAKESOURCES=Makefile.pre.in Setup.in
_MAKEFILES=$(_MAKETARGETS) $(_MAKESOURCES)  Makefile.boot

$(_MAKETARGETS): $(_MAKESOURCES)
	$(EVAL) make -f Makefile.pre.in boot PYTHON=$(PYTHON)

boot.md5: $(_MAKEFILES)
	md5sum $(_MAKEFILES) >boot.md5

valid: spam.so _debug_memory.so

spam.so _debug_memory.so: boot.md5
	# Remove setting OPT, post debugging.
	$(EVAL) make OPT="-g -Wall -Wstrict-prototypes"
