# Makefile for source rpm: httpd
# $Id: Makefile,v 1.1 2004/09/09 06:08:42 cvsdist Exp $
NAME := httpd
SPECFILE = $(firstword $(wildcard *.spec))
UPSTREAM_CHECKS = asc

include ../common/Makefile.common
