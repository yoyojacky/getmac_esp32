#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import commands 

print("please connect ESP32 to USB port...")
while True:
    status,feedback = commands.getstatusoutput('ls /dev/tty.SLAB_USBtoUART')
    #print(status)
    if status == 0:
	print("detected an esp32 device")
        mac = os.popen('sudo esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART read_mac| grep MAC |uniq').read()
        try:
            with open('maclist.txt', 'a') as f:
                f.write(mac)
                f.write('\n')
		print("Mac %s has been record." %mac)
		print("you have 5 seconds to remove esp32")
        	time.sleep(5)
        except KeyboardInterrupt as e:
            f.close()
    else: 
        print('device is not ready...')
