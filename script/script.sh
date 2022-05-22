#!/bin/bash

FETCH_APPS=()
for item in $(jq -c .apps[].name script/apps.json| jq tostring)
do
  FETCH_APPS+=($item)
done
echo ${FETCH_APPS[@]}