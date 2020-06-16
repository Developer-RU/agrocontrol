#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb, time, gc, requests, json, time
from datetime import datetime

while True :

	try:

		db = MySQLdb.connect("localhost", "root", "23111983", "data")
		cursor = db.cursor()
	
		sql = "SELECT * FROM `db` WHERE `send` < 1  ORDER BY `id` DESC LIMIT 10"
		cursor.execute(sql)
		records = cursor.fetchall()

		
		if cursor.rowcount  > 0 :

			_id = []

			str_json = '{"device":"raspberry1","array":['
			for row in records :
				id, timestamp, lat, lon, rfid, wet, s1, s2, s3, s4, send, backup = row
				str_json = str_json + '{"time":"' + str(timestamp) + '","lat":"' + str(lat) + '","lon":"' + str(lon) + '","RFID":"' + str(rfid) + '","wet":"' + str(wet) + '","sensors":{"s1":"' + str(s1) + '","s2":"' + str(s2) + '","s3":"' + str(s3) + '","s4":"' + str(s4) + '"}}'
				str_json = str_json + ','

				_id.append(id)

			str_json = str_json[:-1]
			str_json = str_json + ']}'
	
			dt_json = json.loads(str_json)
	
			req = requests.post('http://94.181.44.80:8000/json', data = dt_json) 
			status_code = req.status_code   # 200

			if int(status_code) == 200 :

				for row in range(0, len(_id)) :

					sql = "UPDATE `db` SET `send` = '1' WHERE `db`.`id` = %d" % (_id[row])
					cursor.execute(sql)

				db.commit()
		
		else :
			
			time.sleep(1)

		db.close()
		gc.collect()

	except :

		time.sleep(1)
		
	time.sleep(1)
