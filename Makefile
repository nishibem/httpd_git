# Makefile for source rpm: httpd
# $Id$
NAME := httpd
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
