BeagleBone Black Entry Alarm
=============================

Objective
---------
Door entry alarm that uses a BeagleBone Black microcontroller to monitor the opening &amp; closing of a door.

Components
----------
* BeagleBone Black (BBB)
* BBB Power Supply
* Magnetic Door Alarm (used [this model](http://www.harborfreight.com/door-window-entry-alarm-94983.html) from Harbor Freight, cost $4.49 in a two-pack)
* Small prototyping breadboard
* (1) 100 Ohm resistor
* (1) 220 Ohm resistor
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
...