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
from kittentts import KittenTTS

init = "QTTS_INIT" in os.environ

if init:
  input = "hello"
else:
  input = sys.stdin.read()
  stdout = sys.stdout
  sys.stdout = open(os.devnull, "w")

m = KittenTTS("KittenML/kitten-tts-nano-0.1")

audio = m.generate(input, voice='expr-voice-2-f' )
audio = np.asarray(audio, dtype=np.float32)
audio = audio.tobytes()
if not init:
  stdout.buffer.write(audio)
