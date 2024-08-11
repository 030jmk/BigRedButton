# BigRedButton
A tiny Raspberry Pi project that plays random audio responses from a collection of audio files, simulating the classic Magic Eight Ball game by pressing a big red button instead of shacking something.


# Fun because
- Hold the big red button to hear a random response.
- Optional: Add your own audio files.

# Step by Step
1. Clone the Repository:
```
git clone https://github.com/030jmk/BigRedButton.git
```
3. Install Dependencies:
```
sudo apt-get install sox libsox-fmt-mp3
```
3. Add Audio Files: Place .wav and .mp3 files in the audio folder.
4. Connect a Button: Use GPIO pin 26 and one of the Ground pins on the Raspberry Pi.
5. Connect a speaker to the 3.5mm audio output jack (of an adapter).
6. If external amplifier or sound card is used, set the correct output with. Find the available devices with `aplay -l` which may look like so:
```
**** List of PLAYBACK Hardware Devices ****
card 0: vc4hdmi [vc4-hdmi], device 0: MAI PCM i2s-hifi-0 [MAI PCM i2s-hifi-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: Headset [Logitech G430 Gaming Headset], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
7. Edit /etc/asound.conf with `sudo nano /etc/asound.conf` and use the following configuration to set the USB audio device as the default (since the USB audio device is card 1 it would then look like so:
```
pcm.!default {
    type hw
    card 1
    device 0
}

ctl.!default {
    type hw
    card 1
}
```
9. Save the file and exit the editor (in nano, CTRL + X, then Y, and Enter).

8. Run the Script for testing purposes
```
python BigRedButton/redbutton.py
```


# Automated start and restart
1. Copy the .service file to the systemd system directory:
```
sudo cp redbutton.service /etc/systemd/system/
```
2. Reload the systemd daemon to recognize the new service file:
```
sudo systemctl daemon-reload
```
3. Enable and start the service to start on boot:
```
sudo systemctl enable redbutton.service
sudo systemctl start redbutton.service

```
4. Check the status of the service to ensure it's running:
```
sudo systemctl status redbutton.service
```
5. Restart the system
```
sudo reboot
```
