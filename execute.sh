#!/usr/bin/env bash

author=${AUTHOR}

echo "Search for author ${author}"

scrapy crawl pub_nlm --nolog

echo "Search complete"