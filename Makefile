# Makefile for source rpm: httpd
# $Id: Makefile,v 1.4 2004/10/13 10:44:51 jorton Exp $
NAME := httpd
SPECFILE = $(firstword $(wildcard *.spec))
UPSTREAM_CHECKS = asc

include ../common/Makefile.common

migration.html: migration.xml html.xsl
	xmlto -x html.xsl html-nochunks migration.xml

view-migration: migration.html
	gnome-moz-remote `pwd`/migration.html

ALL_PATCHES := $(wildcard *.patch)

status.xml: $(ALL_PATCHES) mkstatus.sh
	@./mkstatus.sh $(ALL_PATCHES) > $@

status.html: status.xml status-html.xsl
	@xsltproc status-html.xsl $< > $@

view-status: status.html
	gnome-moz-remote `pwd`/$<
