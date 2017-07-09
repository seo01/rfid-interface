import subprocess
import time
import csv
import argparse

cleanup = []
bigmap = {}
mdir = None
tsvfile = None

def parseCommandLine():
	global mdir
	global tsvfile
	parser = argparse.ArgumentParser(description='RFID Mac OS Interface.')
	parser.add_argument('--mdir', help='directory containing media.')
	args = parser.parse_args()
	mdir = args.mdir
	tsvfile = '%s/%s' % (mdir,'data.tsv')

def readfile():
	with open(tsvfile) as tsv:
		for line in csv.reader(tsv, dialect="excel-tab"):
			k = line[0]
			v = line[1]
			args = line[2:]
			bigmap[k] = [v,args]


def play(dir,track):
	stop()
	args = ['afplay', '%s/%s' % (dir,track)]
	proc = subprocess.Popen(args)
	def clean():
		proc.terminate()
	cleanup.append(clean)

def stop():
	while cleanup:
		f = cleanup.pop()
		f()

def getFocus():
	args = ['osascript', '-e', 'tell app "Terminal"', '-e', 'activate', '-e', 'end tell']
	proc = subprocess.Popen(args)

def reSize():
	#TODO: Pull dimensions into args
	args = ['osascript',
			'-e', 'tell app "Terminal" to tell window 1',
			'-e', 'set b to bounds',
			'-e', 'set item 1 of b to 0',
			'-e', 'set item 2 of b to 0',
			'-e', 'set item 3 of b to 1200',
			'-e', 'set item 4 of b to 60',
			'-e', 'set bounds to b',
			'-e', 'end']
	proc = subprocess.Popen(args)

def init():
	parseCommandLine()
	getFocus() #TODO: May need an additional thread in the background to keep focus
	reSize()
	readfile()
	print bigmap

def run():
	while True:
		x = raw_input("Input:")
		if x in bigmap:
			if bigmap[x][0] == "play":
				play(mdir,bigmap[x][1][0])
			if bigmap[x][0] == "stop":
				stop()

init()
run()