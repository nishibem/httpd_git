# Makefile for source rpm: httpd
# $Id: Makefile,v 1.2 2004/09/15 15:09:00 jorton Exp $
NAME := httpd
SPECFILE = $(firstword $(wildcard *.spec))
UPSTREAM_CHECKS = asc

include ../common/Makefile.common

migration.html: migration.xml html.xsl
	xmlto -x html.xsl html-nochunks migration.xml

migration-view: migration.html
	gnome-moz-remote `pwd`/migration.html

