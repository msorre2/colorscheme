#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ANSI color scheme script featuring various art.
#
# Inspired by various posts on: http://crunchbang.org/forums/viewtopic.php?pid=126921%23p126921#p126921
# Python version by @gardaud
#
import argparse

#define color escape sequence
clear = '\033[0m'
bold = '\033[1m'

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
purple = '\033[95m'
cyan = '\033[96m'
white = '\033[90m'

#available art
invaders = "\
 {2}  ▀▄   ▄▀     {3} ▄▄▄████▄▄▄    {4}  ▄██▄     {5}  ▀▄   ▄▀     {6} ▄▄▄████▄▄▄    {7}  ▄██▄  {0}\n\
 {2} ▄█▀███▀█▄    {3}███▀▀██▀▀███   {4}▄█▀██▀█▄   {5} ▄█▀███▀█▄    {6}███▀▀██▀▀███   {7}▄█▀██▀█▄{0}\n\
 {2}█▀███████▀█   {3}▀▀███▀▀███▀▀   {4}▀█▀██▀█▀   {5}█▀███████▀█   {6}▀▀███▀▀███▀▀   {7}▀█▀██▀█▀{0}\n\
 {2}▀ ▀▄▄ ▄▄▀ ▀   {3} ▀█▄ ▀▀ ▄█▀    {4}▀▄    ▄▀   {5}▀ ▀▄▄ ▄▄▀ ▀   {6} ▀█▄ ▀▀ ▄█▀    {7}▀▄    ▄▀{0}\n\
\n\
 {1}{2}▄ ▀▄   ▄▀ ▄   {3} ▄▄▄████▄▄▄    {4}  ▄██▄     {5}▄ ▀▄   ▄▀ ▄   {6} ▄▄▄████▄▄▄    {7}  ▄██▄  {0}\n\
 {1}{2}█▄█▀███▀█▄█   {3}███▀▀██▀▀███   {4}▄█▀██▀█▄   {5}█▄█▀███▀█▄█   {6}███▀▀██▀▀███   {7}▄█▀██▀█▄{0}\n\
 {1}{2}▀█████████▀   {3}▀▀▀██▀▀██▀▀▀   {4}▀▀█▀▀█▀▀   {5}▀█████████▀   {6}▀▀▀██▀▀██▀▀▀   {7}▀▀█▀▀█▀▀{0}\n\
 {1}{2} ▄▀     ▀▄    {3}▄▄▀▀ ▀▀ ▀▀▄▄   {4}▄▀▄▀▀▄▀▄   {5} ▄▀     ▀▄    {6}▄▄▀▀ ▀▀ ▀▀▄▄   {7}▄▀▄▀▀▄▀▄{0}\n\
\n\
\n\
                                     {3}▌{0}\n\
\n\
                                   {3}▌{0}\n\
\n\
                              {3}    ▄█▄    {0}\n\
                              {3}▄█████████▄{0}\n\
                              {3}▀▀▀▀▀▀▀▀▀▀▀{0}\n\
"

abcdef = "\
{1}{2}  ██████  {0} {1}{3}██████  {0}{1}{4}   ██████{0} {1}{5}██████ {0}  {1}{6}  ██████{0} {1}{7}  ███████{0}\n\
{1}{2}  ████████{0} {1}{3}██    ██ {0}{1}{4}██ {0}      {1}{5}██    ██{0} {1}{6}██████ {0} {1}{7} █████████{0}\n\
{2}  ██  ████{0} {3}██  ████{0}{4} ████    {0} {5}████  ██{0} {6}████ {0}    {7}█████ {0}\n\
{2}  ██    ██{0} {3}██████ {0}{4}  ████████{0} {5}██████ {0}  {6}████████{0} {7}██ {0}\n\
"

pacman = "\
{4}  ▄███████▄{0}   {2}  ▄██████▄{0}    {3}  ▄██████▄{0}    {5}  ▄██████▄{0}    {6}  ▄██████▄{0}    {7}  ▄██████▄{0}\n\
{4}▄█████████▀▀{0}  {2}▄{8}█▀█{2}██{8}█▀█{2}██▄{0}  {3}▄{8}█▀█{3}██{8}█▀█{3}██▄{0}  {5}▄{8}█▀█{5}██{8}█▀█{5}██▄{0}  {6}▄{8}█▀█{6}██{8}█▀█{6}██▄{0}  {7}▄{8}█▀█{7}██{8}█▀█{7}██▄{0}\n\
{4}███████▀{0}      {2}█{8}▄▄█{2}██{8}▄▄█{2}███{0}  {3}█{8}▄▄█{3}██{8}▄▄█{3}███{0}  {5}█{8}▄▄█{5}██{8}▄▄█{5}███{0}  {6}█{8}▄▄█{6}██{8}▄▄█{6}███{0}  {7}█{8}▄▄█{7}██{8}▄▄█{7}███{0}\n\
{4}███████▄{0}      {2}████████████{0}  {3}████████████{0}  {5}████████████{0}  {6}████████████{0}  {7}████████████{0}\n\
{4}▀█████████▄▄{0}  {2}██▀██▀▀██▀██{0}  {3}██▀██▀▀██▀██{0}  {5}██▀██▀▀██▀██{0}  {6}██▀██▀▀██▀██{0}  {7}██▀██▀▀██▀██{0}\n\
{4}  ▀███████▀{0}   {2}▀   ▀  ▀   ▀{0}  {3}▀   ▀  ▀   ▀{0}  {5}▀   ▀  ▀   ▀{0}  {6}▀   ▀  ▀   ▀{0}  {7}▀   ▀  ▀   ▀{0}\n\
\n\
{1}{4}  ▄███████▄   {2}  ▄██████▄    {3}  ▄██████▄    {5}  ▄██████▄    {6}  ▄██████▄    {7}  ▄██████▄{0}\n\
{1}{4}▄█████████▀▀  {2}▄{8}█▀█{2}██{8}█▀█{2}██▄  {3}▄{8}█▀█{3}██{8}█▀█{3}██▄  {5}▄{8}█▀█{5}██{8}█▀█{5}██▄  {6}▄{8}█▀█{6}██{8}█▀█{6}██▄  {7}▄{8}█▀█{7}██{8}█▀█{7}██▄{0}\n\
{1}{4}███████▀      {2}█{8}▄▄█{2}██{8}▄▄█{2}███  {3}█{8}▄▄█{3}██{8}▄▄█{3}███  {5}█{8}▄▄█{5}██{8}▄▄█{5}███  {6}█{8}▄▄█{6}██{8}▄▄█{6}███  {7}█{8}▄▄█{7}██{8}▄▄█{7}███{0}\n\
{1}{4}███████▄      {2}████████████  {3}████████████  {5}████████████  {6}████████████  {7}████████████{0}\n\
{1}{4}▀█████████▄▄  {2}██▀██▀▀██▀██  {3}██▀██▀▀██▀██  {5}██▀██▀▀██▀██  {6}██▀██▀▀██▀██  {7}██▀██▀▀██▀██{0}\n\
{1}{4}  ▀███████▀   {2}▀   ▀  ▀   ▀  {3}▀   ▀  ▀   ▀  {5}▀   ▀  ▀   ▀  {6}▀   ▀  ▀   ▀  {7}▀   ▀  ▀   ▀{0}\n\
"

art_choices = {
  'abcdef': abcdef,
  'invaders': invaders,
  'pacman': pacman,
}


def main(art_choice):
  import sys

  art = art_choices[art_choice]
  print >> sys.stdout, art.format(clear, bold, red, green, yellow, blue, purple, cyan, white)
