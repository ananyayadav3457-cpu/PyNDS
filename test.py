import pynds
from pynds import config

# Enable audio BEFORE loading ROM
config.set_emulate_audio(1)
config.set_audio_16_bit(1)

nds = pynds.PyNDS('rom/SoulSilver.nds')
nds.open_window()

for i in range(2000):  # run 180 frames = ~3 seconds
    nds.tick()
    nds.render()

nds.close_window()
print('Done!')