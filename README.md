# BigRedButton
A tiny Raspberry Pi project that plays random audio responses from a collection of audio files, simulating the classic Magic Eight Ball game by pressing a big red button instead of shacking something.


# Fun because
- Hold the big red button to hear a random response.
- Optional: Add your own audio files.

# 
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
6. (optional) use and external amplifier and set the correct audio output with `sudo raspi-config`.
7. Run the Script.
```
python red.py
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
3. Enable the service to start on boot:
```
sudo systemctl enable redbutton.service
```
4. Check the status of the service to ensure it's running:
```
sudo systemctl status redbutton.service
```

