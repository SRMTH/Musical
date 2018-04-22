import time
import os

note={
	'C'  : 523.25,
	'C#' : 554.37,
	'D'  : 587.33,
	'D#' : 622.25,
	'E'  : 659.25,
	'F'  : 698.46,
	'F#' : 739.99,
	'G'  : 783.99,
	'G#' : 830.61,
	'A'  : 880.00,
	'A#' : 932.33,
	'B'  : 987.77,
	'C+' : 1046.50
      }


def play_music(song):
	li=song.split('|')
	for l in li:
		t=l.split()
		os.system('play --no-show-progress --null --channels 1 synth '+str(t[1])+' sine '+str(note[t[0]]) )
		print l


if __name__=='__main__':
	play_music()
