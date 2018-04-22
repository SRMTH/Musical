#l- 22 cm, r- 31cm

import time
import os
import songs
import pypot.dynamixel


notes={
	'G-' : {1:-50, 3:-93},
	'A-' : {1:-53, 3:-91},
	'B-' : {1:-60, 3:-93},
	'C'  : {1:-75, 3:-105},		'C#' : {1:-19, 3:-35},
	'D'  : {1:-75, 3:-100},		'D#' : {1:-22, 3:-34},
	'E'  : {1:-80, 3:-99.5},
	'F'  : {1:-80, 3:-94},		'F#' : {1:-22, 3:-25},
	'G'  : {1:-80, 3:-88},		'G#' : {1:-21.5, 3:-18.5},
	'A'  : {1:-80, 3:-83.5},	'A#' : {1:-20, 3:-11.5},
	'B'  : {1:-80, 3:-78},
	'C+' : {1:-78, 3:-72}
      }

def init():
	ports=pypot.dynamixel.get_available_ports()		
	print(ports)
	if not ports :
		raise IOError("no ports found bruh!")
	print "Connecting to ",ports[0]
	global dxl
	dxl=pypot.dynamixel.DxlIO(ports[0])
	ids=dxl.scan(range(30))
	print ids
	print dxl.get_present_position(ids)
	dxl.set_moving_speed({1:100,3:100,5:100})
	dxl.set_goal_position(notes['E'])

def hit(l):
	if '#' in l:
		time.sleep(0.4)
		dxl.set_goal_position({5:87.5})			#no minor notes
	else:
		time.sleep(0.1)
		dxl.set_goal_position({5:96.5})
	time.sleep(0.2)
	dxl.set_goal_position({5:93})


def play_music(song):
	li=song.split()
	for l in li:
		try:
			time.sleep(float(l))
		except ValueError:
			dxl.set_goal_position(notes[l])
			time.sleep(0.3)
			hit(l)
			print l

if __name__=='__main__':
	init()
	raw_input()
	play_music(songs.harry_potter)
	'''while True:
		l=raw_input()
		dxl.set_goal_position(notes[l])
		time.sleep(0.9)
		hit(l)'''
