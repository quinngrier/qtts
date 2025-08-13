#
# The authors of this file have waived all copyright and
# related or neighboring rights to the extent permitted by
# law as described by the CC0 1.0 Universal Public Domain
# Dedication. You should have received a copy of the full
# dedication along with this file, typically as a file
# named <CC0-1.0.txt>. If not, it may be available at
# <https://creativecommons.org/publicdomain/zero/1.0/>.
#

FROM python:3.10

RUN : \
  && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -q -y update \
  && apt-get -q -y install \
       espeak-ng \
;

RUN pip install \
  kokoro==0.9.4 \
  numpy \
  pyjson5 \
;

COPY \
  main.py \
  voices.json5 \
/

RUN QTTS_INIT= python /main.py
