# main.py

'''
  TODO:
    - add time segments for shows/commercials
      - morning/eventing, saturdays, etc
    - add seasons
      - holiday specials
    - get ffmpeg to work
    - stream out to ip
    - stream out to hdmi out
    - read in a file with list of shows and commercials
        so this can be more universal friendly
'''

import os
import time
#import ffmpeg
#import ffmpeg_streaming
import datetime
from random import seed
from random import randint
import sys

class Show:
  def __init__(self, name, path):
    self.name = name
    self.path = path
    self.episodes = []
    self.it = 0

  def AddEpisodes(self, path):
    os.chdir(path)

    episodes = os.listdir('.')

    for e in episodes:
      if os.path.isdir(e):
        self.AddEpisodes(e)
      else:
        exts = e.split('.')
        if exts[len(exts) - 1] == 'mp4' or exts[len(exts) - 1] == 'avi' or exts[len(exts) - 1] == 'mpg' or exts[len(exts) - 1] == 'wmv':
          self.episodes.append(os.getcwd() + '/' + e)
        else:
          print('WARNING: ' + e + ' is invalid')

    os.chdir('..')

class Commercial:
  def __init__(self, category, path):
    self.category = category
    self.path = path
    self.spots = []

  def AddSpots(self, path):
    os.chdir(path)

    spots = os.listdir('.')

    for s in spots:
      if os.path.isdir(s):
        self.AddSpots(s)
      else:
        exts = s.split('.')
        if exts[len(exts) - 1] == 'mp4' or exts[len(exts) - 1] == 'avi' or exts[len(exts) - 1] == 'mpg' or exts[len(exts) - 1] == 'wmv':
          self.spots.append('commercials/' + self.path + '/' + s)
        else:
          print('WARNING: ' + s + ' is invalid')

    os.chdir('..')

# globals
shows = []
commercials = []

def Initialize():
  # initialize tv shows
  angelaa = Show('Angela Anaconda', 'angela_anaconda')
  shows.append(angelaa)
  unfabulous = Show('Unfabulous', 'unfabulous')
  shows.append(unfabulous)
  rockosml = Show('Rocko\'s Modern Life', 'rockos_modern_life')
  shows.append(rockosml)
  cnsorig = Show('CNS Originals', 'cns_originals')
  shows.append(cnsorig)

  # populate episodes
  os.chdir('tv')

  angelaa.AddEpisodes(angelaa.path)
  unfabulous.AddEpisodes(unfabulous.path)
  rockosml.AddEpisodes(rockosml.path)
  cnsorig.AddEpisodes(cnsorig.path)

  os.chdir('..')

  # initialize commercials
  cBumps = Commercial('bumps', 'bumps')
  commercials.append(cBumps)
  cFood = Commercial('food', 'food')
  commercials.append(cFood)
  cProducts = Commercial('products', 'products')
  commercials.append(cProducts)
  cPsa = Commercial('psa', 'psa')
  commercials.append(cPsa)
  cShows = Commercial('shows', 'shows')
  commercials.append(cShows)
  cToys = Commercial('toys', 'toys')
  commercials.append(cToys)

  # populate commercial spots
  os.chdir('commercials')

  cBumps.AddSpots(cBumps.path)
  cFood.AddSpots(cFood.path)
  cProducts.AddSpots(cProducts.path)
  cPsa.AddSpots(cPsa.path)
  cShows.AddSpots(cShows.path)
  cToys.AddSpots(cToys.path)

  os.chdir('..')

def Run():
  count = 0
  com_count = 0
  seed(sys.argv[1])

  while count < 13:
    if com_count < 2:
      com = randint(0, len(commercials))
      spt = randint(0, len(commercials[com].spots))
      spot = commercials[com].spots[spt]
      print('num commercials: ' + str(len(commercials)) + ' commercial: ' + str(com))
      print('num spots: ' + str(len(commercials[com].spots)) + ' spot: ' + str(spt))
      os.system('ffmpeg -re -i \'' + spot + '\' -f mpegts \"udp://127.0.0.1:2002\"')
      com_count = com_count + 1
    else:
      shw = randint(0, len(shows))
      ep = randint(0, len(shows[shw].episodes))
      print('num shows: ' + str(len(shows)) + ' show: ' + str(shw))
      print('num episodes: ' + str(len(shows[shw].episodes)) + ' ep: ' + str(ep))
      episode = shows[shw].episodes[ep]
      os.system('ffmpeg -re -i \'' + episode + '\' -f mpegts \"udp://127.0.0.1:2002\"')
      com_count = 0
    count = count + 1


def main():

  # add tv shows and commercials
  Initialize()

  if sys.argv[1] == 'print':
    for ep in shows[2].episodes:
      print(ep)
  else:
    # air the channel
    Run()

if __name__ == "__main__":
  main()
