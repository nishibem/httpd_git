# Makefile for source rpm: httpd
# $Id: Makefile,v 1.6 2004/11/18 11:59:52 jorton Exp $
NAME := httpd
SPECFILE = $(firstword $(wildcard *.spec))
UPSTREAM_CHECKS = asc

include ../common/Makefile.common

migration.html: migration.xml html.xsl
	xmlto -x html.xsl html-nochunks migration.xml

view-migration: migration.html
	gnome-moz-remote `pwd`/migration.html

