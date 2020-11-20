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
'''
    
import os
import time
#import ffmpeg
#import ffmpeg_streaming
import datetime
from random import seed
from random import randint

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
          self.episodes.append('tv/' + self.path + '/' + e)
        else:
          print('WARNING: ' + e + ' is invalid')
    
    os.chdir('..')

class Commercial:
  def __init__(self, category, path):
    self.category = category
    self.path = path
    self.spots = []
    self.it = 0

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
  commercial_count = 0
  seed(1)

  while commercial_count < 4:
    i = randint(0, len(commercials))
    spot = commercials[i].spots[commercials[i].it]
    os.system('ffmpeg -re -i \'' + spot + '\' -f mpegts \"udp://127.0.0.1:2002\"')
    commercials[i].it = commercials[i].it + 1
    commercial_count = commercial_count + 1

'''
  for commercial in commercials:
      for spot in commercial.spots:
        os.system('ffmpeg -re -i \'' + spot + '\' -f mpegts \"udp://127.0.0.1:2002\"')
        time.sleep(1)
'''

def main():

  # add tv shows and commercials
  Initialize()

  # air the channel
  Run()

if __name__ == "__main__":
  main()
