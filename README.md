BeagleBone Black Entry Alarm
=============================

Objective
---------
Door entry alarm that uses a BeagleBone Black microcontroller to monitor the opening &amp; closing of a door.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=eaGEvw2cZl8" target="_blank"><img src="http://img.youtube.com/vi/eaGEvw2cZl8/0.jpg" alt="Hardware overview video" width="240" height="180" border="10"/></a>

Components
----------
* BeagleBone Black (BBB)
* BBB Power Supply
* Magnetic Door Alarm (used [this model](http://www.harborfreight.com/door-window-entry-alarm-94983.html) from Harbor Freight, cost $4.49 in a two-pack)
* Small prototyping breadboard
* (1) 10K Ohm resistor
* Wire in various colors

Tools
-----
* Multimeter with test leads
* Dremel tool with attachment to cut plastic
* Soldering Iron
* Solder
* Desoldering Braid (optional)

Steps
-----
1. Open the magnetic door alarm case
1. Cut wires from speaker
1. Desolder the wires running from circuit board to the speaker
1. Solder two new, longer wires to the circuit board
1. Use a Dremel to create a small hole in the alarm case to route the new wires outside
1. Seal up the case
1. Connect the wires to the breadboard in a voltage divider configuration with the resistors, ensuring that voltage doesn’t exceed 1.3V
1. Use a digital multimeter to verify that the alarm triggers about a 200 milli-volt rise in voltage across the voltage divider circuit wires when the magnet is removed.
1. Connect the voltage divider outputs to analog input pins on the BeagleBone Black
1. Apply power to the BBB
1. SSH into the BBB
1. Install Python dependencies:
    ```shell
    sudo apt-get update
    sudo apt-get install python-pip
    git clone https://github.com/bear/python-twitter.git
    cd python-twitter/
    sudo pip install -r requirements.txt
    python setup.py build
    sudo python setup.py install
    sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus -y
    sudo easy_install -U distribute
    sudo pip install Adafruit_BBIO
    ```

13. Clone this project into the ubuntu home directory: ```git clone https://github.com/urlgrey/beaglebone_entry_alarm.git```
1. Edit the settings file: ```vi ~/beaglebone_entry_alarm/settings.py```
1. Add an entry to the ```/etc/rc.local``` file, before the ```exit``` statement, to start the script on boot:
```shell
/home/ubuntu/beaglebone_entry_alarm/door_alarm.sh &> /var/log/door_alarm.log
```
