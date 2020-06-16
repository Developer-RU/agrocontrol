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

		db = MySQLdb.connect("localhost", "root", "23111983", "data")
		cursor = db.cursor()
	
		timestamp = 1545730073
		dt_object = datetime.fromtimestamp(timestamp)

		#print(dt_object.strftime('%Y-%m-%d %H:%M:%S'))

		sql = "INSERT INTO `db` ( `id`, `timestamp`, `lat`, `lon`, `rfid`, `wet`, `s1`, `s2`, `s3`, `s4` ) VALUES ( NULL, '" + dt_object.strftime('%Y-%m-%d %H:%M:%S') + "', '%s', '%s', '%s', '%d', '%d', '%d', '%d', '%d' ) " %  ( '59.8879318237', '50.8879318237', '0', 20, 123, 234, 345, 456)
		cursor.execute(sql)

		db.commit()
		db.close()


		rnd = random.randrange(1, 11, 2) 
	
		str_json = '{"device":"raspberry1","array":['
		for n in range(0, rnd) :
			str_json = str_json + '{"time":"1592156705234","lat":"59.8879318237","lon":"54.589931488","RFID":"0","wet":"0","sensors":{"s1":"0","s2":"0","s3":"0","s4":"0"}}'
			str_json = str_json + ','
		
		str_json = str_json[:-1]
		str_json = str_json + ']}'
	
	
		#str_json = '{"device":"raspberry1","array":[{"time":"1592156705234","lat":"59.8879318237","lon":"54.589931488","RFID":"0","wet":"0","sensors":{"s1":"0","s2":"0","s3":"0","s4":"0"}},{"time":"1592156705234","lat":"59.8879318237","lon":"54.589931488","RFID":"1","wet":"0","sensors":{"s1":"0","s2":"0","s3":"0","s4":"0"}}]}'
	
	
		dt_json = json.loads(str_json)
	
	
		req = requests.post('http://94.181.44.80:8000/json', data = dt_json) 
	 
		encoding = req.encoding      	# 'utf-8'
		status_code = req.status_code   # 200
		elapsed = req.elapsed      		# datetime.timedelta(0, 1, 666890)
		url = req.url           		# 'https://tutsplus.com/'
		content = req.content
		text = req.text
		history = req.history      
		headers = req.headers['Content-Type']
	
	
		print ''
		print '---------------------------------------------------------------------------------'
		print text
		print '---------------------------------------------------------------------------------'
		print ''
	

	except :

		time.sleep(1)
		
	time.sleep(1)
