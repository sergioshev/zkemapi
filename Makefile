PYTHON_LIBS=/usr/lib/python2.7
LIB=zkemapi


.phony: all
all: install

.phony: install
install: $(LIB)
	cp -r $(LIB) $(PYTHON_LIBS)


