#!/bin/bash

module="$1"
category="$2"
title="$(echo $category | sed 's/\([A-Z]\)/ \1/g' | sed 's/^\s\+//')"

if [ -z "${module}" ]; then
	echo "ERROR: missing module name." >&2
	exit 1
fi

if [ -z "${module}" ]; then
	echo "ERROR: missing category name." >&2
	exit 1
fi

echo
echo "${title}"
echo "$(echo $title | sed 's/./~/g')"
echo
cat "../staty/${module}.py" |\
    sed -n "/${category}/s/^class \(.*\)(.*):$/.. autoclass:: staty.${module}.\1\n    :members:\n    :undoc-members:\n    :show-inheritance:\n/p"
