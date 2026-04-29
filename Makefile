
PREFIX     := /usr/local

SRC_DIR    := src
BUILD_DIR  := build
LIB_DIR    := $(BUILD_DIR)/lib

PYTHON     := $(shell which python 2>/dev/null)
INSTALL    := $(shell which install 2>/dev/null)
MKDIR      := $(shell which mkdir 2>/dev/null)
ECHO       := $(shell which echo 2>/dev/null)
CAT        := $(shell which cat 2>/dev/null)
GIT        := $(shell which git 2>/dev/null)
RM         := $(shell which rm 2>/dev/null)


PYTHON_VER := $(shell $(PYTHON) --version 2>&1 | awk '{if (/Python/) {split($$2,v,".");print "python"v[1]"."v[2]}}')
INSTALL_DIR = $(INSTALL) -m 755 -d
INSTALL_LIB = $(INSTALL) -m 644 -p
INSTALL_REG = $(INSTALL) -m 644 -p
MKDIR_P     = $(MKDIR) -p
RM_R        = $(RM) -r

PROJECT    := strand
LIBRARY    := strand
VERSION    := $(shell $(GIT) describe --long --tags --always)
CONTACT    := https:\/\/github.com\/bredeson\/strand\/issues
LICENSE    := LICENSE

LIB_TARGETS = $(LIB_DIR)/$(LIBRARY).py

.SUFFIXES:
.SUFFIXES: .py

.PHONY: all install activate clean

all: $(LIB_DIR) $(LIB_TARGETS) activate

$(LIB_DIR):
	@$(MKDIR_P) $@

$(LIB_DIR)/%: $(SRC_DIR)/%
	$(CAT) LICENSE $< >$@

build: $(LIB_DIR) $(LIB_TARGETS)

activate:
	@$(ECHO) 'export PYTHONPATH="$(PREFIX)/lib/$(PYTHON_VER)/site-packages:$$PYTHONPATH";' >activate
	@$(ECHO) '#setenv PYTHONPATH "$(PREFIX)/lib/$(PYTHON_VER)/site-packages:$$PYTHONPATH";' >>activate

install: all
	$(INSTALL_DIR) $(PREFIX)/lib/$(PYTHON_VER)/site-packages
	$(INSTALL_LIB) $(LIB_DIR)/* $(PREFIX)/lib/$(PYTHON_VER)/site-packages
	$(INSTALL_REG) activate $(PREFIX)/

clean:
	-$(RM_R) $(BUILD_DIR)
