import time
import math
from ecoventv2 import Fan

fan=Fan("10.94.0.106","003A00345842570A","1111")

# Set examples
fan.set_param('state','on') #'on','off','togle'
print ( 'state: ' + fan.state )
# fan.set_param('speed','manual') #'low','medium','high','manual'
# print ( 'speed: ' + fan.speed )
# fan.set_param('man_speed', hex(math.ceil( 5 * 255 / 100 )).replace("0x","").zfill(2) ) # hex(math.ceil( speed_in_% * 255 / 100 )).replace("0x","").zfill(2)
# print ( 'man_speed: ' + fan.man_speed )
# fan.set_param('timer_mode','off') # 'off', 'night', 'party'
# print ( 'timer_mode: ' + fan.timer_mode )
# fan.update()
# print ( 'timer_counter: ' + fan.timer_counter )
# fan.set_param('humidity_sensor_state','on') # 'off', 'on', 'togle'
# print ( 'humidity_sensor_state: ' + fan.humidity_sensor_state )
# fan.set_param('relay_sensor_state','off') # 'off', 'on', 'togle'
# print ( 'relay_sensor_state: ' + fan.relay_sensor_state )
# fan.set_param('analogV_sensor_state','off') # 'off', 'on', 'togle'
# print ( 'analogV_sensor_state: ' + fan.analogV_sensor_state )
# fan.set_param('humidity_treshold',hex(60).replace("0x","").zfill(2)) #hex(humidity_in_%).replace("0x","").zfill(2) 
# print ( 'humidity_treshold: ' + fan.humidity_treshold )
# fan.set_param('boost_time', hex(30).replace("0x","").zfill(2) ) # hex(minutes).replace("0x","").zfill(2)
# print ( 'boost_time: ' + fan.boost_time )
#h=0
#m=38
#s=00
#fan.set_param('rtc_time', hex(s).replace("0x","").zfill(2) + hex(m).replace("0x","").zfill(2) + hex(h).replace("0x","").zfill(2))
#print ( 'rtc_time: ' + fan.rtc_time )
#day_in_week=5
#month=10
#day=8
#year=21
#fan.set_param('rtc_date', hex(day).replace("0x","").zfill(2) + hex(day_in_week).replace("0x","").zfill(2) + hex(month).replace("0x","").zfill(2) + hex(year).replace("0x","").zfill(2))
#print ( 'rtc_date: ' + fan.rtc_date )
#fan.set_param('cloud_server_state','off') # 'off', 'on', 'togle'
#print ( 'cloud_server_state: ' + fan.cloud_server_state )
#fan.set_param('airflow','heat recovery') # 'ventilation', 'heat recovery', 'supply'
#print ( 'airflow: ' + fan.airflow )
#fan.set_param('analogV_treshold',hex(50).replace("0x","").zfill(2)) #hex(analogV_treshold_%).replace("0x","").zfill(2) 
#print ( 'analogV_treshold: ' + fan.analogV_treshold )
#h=8
#m=0
#fan.set_param('night_mode_timer',hex(m).replace("0x","").zfill(2) + hex(h).replace("0x","").zfill(2)) 
#print ( 'night_mode_timer: ' + fan.night_mode_timer )
h=4
m=0
fan.set_param('party_mode_timer', hex(m).replace("0x","").zfill(2) + hex(h).replace("0x","").zfill(2)) 
print ( 'party_mode_timer: ' + fan.party_mode_timer )

for i in range (1,8):
    for j in range (1,5):
        fan.do_func(fan.func['read'] , "0077" , hex(i).replace("0x","").zfill(2) + hex(j).replace("0x","").zfill(2)) # value select schedule Day/Period
        print ( 'weekly_schedule_setup: ' + fan.weekly_schedule_setup ) 
        time.sleep(0.2)

#for param in fan.params:
# print ( fan.params[param][0] + ": " + str(getattr ( fan, fan.params[param][0])))
#in python 3, you'll need to cast to list:
# keys = list(i.keys())
#fan.set_state_off();
#time.sleep ( 1 )
#fan.set_state_on();
#fan.set_man_speed(50)
#time.sleep ( 1 )
#fan.update()

# fan.set_speed(1)
# fan.set_state_on();
# fan.set_man_speed(2)
# fan.set_airflow(1)
# print ( fan.state )
# print ( fan.speed )
# print ( fan.man_speed )
# print ( fan.fan1_speed )
# print ( fan.fan2_speed )
# print ( fan.airflow )
