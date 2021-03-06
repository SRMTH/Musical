notes=[
"C-","C-#","D-","D-#","E-","F-","F-#","G-","G-#","A-","A-#","B-",
"C","C#","D","D#","E","F","F#","G","G#","A","A#","B",
"C+","C+#","D+","D+#","E+","F+","F+#","G+","G+#","A+","A+#","B+"
]

def shift(note,num):
	if note=='\n':
		return '\n'
	for i in range(0,36):
		if notes[i]==note:
			return notes[i+num]
	return ' '

def newsong(song,num):
	new_song=''
	song1=song.split(' ')
	for x in song1:
		new_song=new_song+shift(x,num)+' '
	return new_song

song='\
B- E G F# E B A F# \n \
E G F# D F B- \n \
B- E G F# E B D+ C+# C+ \n \
A C+ B A# B G E \n \
G B G B \n \
G C+ B A# F# G B A# C+ B B \n \
G B G B \n \
G D+ C# C+ A C+ B A# B G E \n \
'

song1='\
E D# E G# G# G# \n \
G# G# G# A G# F# \n \
E D# E G# G# G# \n \
G# G# G# A G# F# \n \
E D# E F# F# G# \
'

if __name__=='__main__':
	print song+'\n\n'
	for num in range (-4,8):
		x = newsong(song,num)
		if '#' not in x:
			print x
			print '\n'
