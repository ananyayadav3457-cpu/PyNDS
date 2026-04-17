import pynds,time
rom_path = "rom/SoulSilver.nds"  # path to your .nds file
nds = pynds.PyNDS(rom_path)

nds.open_window(width=512, height=500)  # opens pygame window automatically
while nds.window.running:
    nds.tick()      # runs emulator until next frame
    nds.render()    # renders both screens using built-in window.py
    #time.sleep(0.005)   #time stop 