# btmusic
Quick python scripts for controlling music playback on a phone over bluetooth.

Tested on Arch Linux, but might work elsewhere.

## Configuration
- Ensure that `pulseaudio-bluetooth` is installed.
- Pair your phone (I used bluetoothctl)
- Update `player.py` with the bluetooth address of your phone.
- If not connected, use `connect.py` to connect to your phone.
- Set up some hotkeys to call the individual scripts to play/pause, or skip backward and forward.
- ???
- Profit.
