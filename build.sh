#!/bin/sh
set -e
rm -rf public && mkdir -p public
cp index.html devotions.json public/
for k in $(grep -oE '"[0-9]{4}-[0-9]{2}-[0-9]{2}"' devotions.json | tr -d '"'); do
  mkdir -p public/d/$k && cp index.html public/d/$k/index.html
done
