#
# The authors of this file have waived all copyright and
# related or neighboring rights to the extent permitted by
# law as described by the CC0 1.0 Universal Public Domain
# Dedication. You should have received a copy of the full
# dedication along with this file, typically as a file
# named <CC0-1.0.txt>. If not, it may be available at
# <https://creativecommons.org/publicdomain/zero/1.0/>.
#

import os
import sys
import numpy as np
from kokoro import KPipeline

init = "QTTS_INIT" in os.environ

if init:
  input = "hello"
else:
  input = sys.stdin.read()
  stdout = sys.stdout
  sys.stdout = open(os.devnull, "w")

QTTS_VOICE = os.getenv("QTTS_VOICE", "af_heart")

pipeline = KPipeline(lang_code="a")

generator = pipeline(input, speed=1.25, voice=QTTS_VOICE)

for i, (gs, ps, audio) in enumerate(generator):
  if not init:
    audio = np.asarray(audio, dtype=np.float32)
    audio = audio.tobytes()
    stdout.buffer.write(audio)
