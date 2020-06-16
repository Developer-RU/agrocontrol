#!/usr/bin/python
# -*- coding: utf-8

import MySQLdb, string, time, sys, os, gc, urlparse
import paho.mqtt.client as mqtt


# topics
# 
# device:id:command 
# 
# group:id:command
# 
# (bash)


def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)



client = mqtt.Client()

client.on_connect   = on_connect
client.on_message   = on_message
client.on_publish   = on_publish
client.on_subscribe = on_subscribe

client.on_log       = on_log



client.username_pw_set(username="user",password="231183")
client.connect("212.22.94.252", 1883, 60)


topic = '#'

client.subscribe(topic, 0)
#client.publish(topic, "my message")


#######################db = MySQLdb.connect(host="localhost", user="root", passwd="23111983", db="mosquito", charset='utf8')
#######################cursor = db.cursor()            
#sql = "SELECT * FROM `stats_money` WHERE `type`=%d ORDER BY `id` DESC LIMIT 1" % (int(type))
#cursor.execute(sql)
#######################db.close()


rc = 0

while rc == 0:
    rc = client.loop()
    #print "123"
print("rc: " + str(rc))



#packet_num = 0
#
#while True :
#	result = os.popen("sensors")
#	client.publish("/", ">>>>>>>>>>>> packet_num = " + str(packet_num) + "\n" + str(result.read()))
#	packet_num = packet_num + 1
#	time.sleep(3)



###client.loop_forever()
