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
import pyjson5
import numpy as np
from kokoro import KPipeline

with open("/voices.json5", "r") as f:
  voices = pyjson5.decode_io(f)
for name, voice in voices.items():
  voice["name"] = name

if "QTTS_INIT" in os.environ:
  for voice in voices.values():
    pipeline = KPipeline(lang_code=voice["lang_code"])
    generator = pipeline("hello", voice=voice["name"])
    for i, (gs, ps, audio) in enumerate(generator):
      pass
  sys.exit(0)

input = sys.stdin.read()
stdout = sys.stdout
sys.stdout = open(os.devnull, "w")

QTTS_VOICE = os.getenv("QTTS_VOICE")
if QTTS_VOICE is None:
  xs = [x for x in voices.values() if x.get("default") is True]
  QTTS_VOICE = xs[0]["name"]
voice = voices[QTTS_VOICE]

pipeline = KPipeline(lang_code=voice["lang_code"])

generator = pipeline(input, speed=1.25, voice=voice["name"])

for i, (gs, ps, audio) in enumerate(generator):
  audio = np.asarray(audio, dtype=np.float32)
  audio = audio.tobytes()
  stdout.buffer.write(audio)
