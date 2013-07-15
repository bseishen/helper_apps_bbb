#!/bin/bash

echo 47 > /sys/class/gpio/export
echo out >/sys/class/gpio/gpio47/direction
echo 0 > /sys/class/gpio/gpio47/value
echo "Finished."
