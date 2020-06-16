#!/usr/bin/python
# -*- coding: utf-8

import MySQLdb
import string
import time
import serial
import sys, os, gc
import urlparse
import requests
import json
import random
import time
import io

from datetime import datetime

while True :

	try:

		ser = serial.Serial(
			port='/dev/ttyUSB0',
			baudrate=9600,
			parity=serial.PARITY_ODD,
			stopbits=serial.STOPBITS_TWO,
		  	bytesize=serial.SEVENBITS
		)

		ser.isOpen()

		while True :

			strdata = ""
			while ser.inWaiting() > 0:
				strdata += ser.read(1)
				time.sleep(0.01)

			if strdata != '' :

				obj_json = json.loads(strdata)

				try:

					db = MySQLdb.connect("localhost", "root", "23111983", "data")
					cursor = db.cursor()
		
					timestamp = obj_json["time"]
					dt_object = datetime.fromtimestamp(timestamp)
		
					sql = "INSERT INTO `db` ( `id`, `timestamp`, `lat`, `lon`, `rfid`, `wet`, `s1`, `s2`, `s3`, `s4` ) VALUES ( NULL, '" + str(dt_object) + "', '" + str(obj_json["gps"][0]) + "', '" + str(obj_json["gps"][1]) + "', '" + str(obj_json["rfid"]) + "', " + str(obj_json["hum"]) + ", " + str(obj_json["dist"][0]) + ", " + str(obj_json["dist"][1]) + ", " + str(obj_json["dist"][2]) + ", " + str(obj_json["dist"][3]) + " ) "
					cursor.execute(sql)
	
					db.commit()
					db.close()

				except :

					time.sleep(1)

				time.sleep(1)

	except :

		time.sleep(1)
