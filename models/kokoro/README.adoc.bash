#! /usr/bin/env bash

#
# The authors of this file have waived all copyright and
# related or neighboring rights to the extent permitted by
# law as described by the CC0 1.0 Universal Public Domain
# Dedication. You should have received a copy of the full
# dedication along with this file, typically as a file
# named <CC0-1.0.txt>. If not, it may be available at
# <https://creativecommons.org/publicdomain/zero/1.0/>.
#

set -E -e -o pipefail -u -x || exit $?
trap exit ERR

dir=$0
if [[ $dir != /* ]]; then
  dir=./$dir
fi
dir=${dir%/*}
readonly dir

voices_list=$(
  json5 "$dir/voices.json5" | jq -r '.
    | to_entries
    | map(""
        + "* "
        + "`" + .key + "`"
        + (if .value.default then " (default)" else "" end)
        + ": "
        + (.value.lang_code | if false then ""
           elif . == "a" then "American English"
           elif . == "b" then "British English"
           elif . == "e" then "Spanish"
           elif . == "f" then "French"
           elif . == "h" then "Hindi"
           elif . == "i" then "Italian"
           elif . == "j" then "Japanese"
           elif . == "p" then "Brazilian Portuguese"
           elif . == "z" then "Mandarin Chinese"
           else error end)
      )
    | join("\n")
  '
)
readonly voices_list

new_content=$(
  awk \
    -v voices_list="$voices_list" \
    '
      {
        if (/^\/\/ end_voices_list$/) {
          print voices_list;
          in_voices_list = 0;
        }
        if (!in_voices_list) {
          print;
        }
        if (/^\/\/ begin_voices_list$/) {
          in_voices_list = 1;
        }
      }
    ' \
    "$dir/README.adoc" \
  ;
)
readonly new_content

printf '%s\n' "$new_content" >"$dir/README.adoc"
