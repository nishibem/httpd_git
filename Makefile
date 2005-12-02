# Makefile for source rpm: httpd
# $Id: Makefile,v 1.2 2005/11/30 12:50:30 jorton Exp $
NAME := httpd
SPECFILE = $(firstword $(wildcard *.spec))
UPSTREAM_CHECKS = asc

include ../common/Makefile.common

migration.html: migration.xml html.xsl
	xmlto -x html.xsl html-nochunks migration.xml

view-migration: migration.html
	gnome-moz-remote `pwd`/migration.html

