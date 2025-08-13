#
# The authors of this file have waived all copyright and
# related or neighboring rights to the extent permitted by
# law as described by the CC0 1.0 Universal Public Domain
# Dedication. You should have received a copy of the full
# dedication along with this file, typically as a file
# named <CC0-1.0.txt>. If not, it may be available at
# <https://creativecommons.org/publicdomain/zero/1.0/>.
#

# TODO: Maybe don't need QTTS_INIT for this model.

import os
import sys
import numpy as np
from kittentts import KittenTTS

if "QTTS_INIT" in os.environ:
  m = KittenTTS("KittenML/kitten-tts-nano-0.1")
  m.generate("hello", voice="expr-voice-2-f")
  sys.exit(0)

stdout = sys.stdout
sys.stdout = open(os.devnull, "w")

input = sys.stdin.read()

QTTS_VOICE = os.getenv("QTTS_VOICE", "expr-voice-2-f")

m = KittenTTS("KittenML/kitten-tts-nano-0.1")

audio = m.generate(input, voice=QTTS_VOICE)
audio = np.asarray(audio, dtype=np.float32)
audio = audio.tobytes()
stdout.buffer.write(audio)
