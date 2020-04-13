#!/usr/bin/env bash

author=${AUTHOR}

echo "Search for author ${author}"

scrapy crawl nlm --nolog

echo "Search complete"