# Makefile for source rpm: httpd
# $Id: Makefile,v 1.3 2004/09/17 10:28:46 jorton Exp $
NAME := httpd
SPECFILE = $(firstword $(wildcard *.spec))
UPSTREAM_CHECKS = asc

include ../common/Makefile.common

migration.html: migration.xml html.xsl
	xmlto -x html.xsl html-nochunks migration.xml

migration-view: migration.html
	gnome-moz-remote `pwd`/migration.html

ALL_PATCHES := $(wildcard *.patch)

status.xml: $(ALL_PATCHES)
	@./mkstatus.sh $(ALL_PATCHES) > $@

status.html: status.xml status-html.xsl
	@xsltproc status-html.xsl $< > $@

view-status: status.html
	gnome-moz-remote `pwd`/$<
