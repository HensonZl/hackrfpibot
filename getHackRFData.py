import subprocess #allows for the use of terminal commands to be executed
import csv #to enable the ability to read and write CSV files
import json #to enable the ability to read and write JSON files
  
class HackRF: #init function for the hackrf see the server file for explination
  def __init__(self, dataPath, range, bandwidth):
    self.dataPath = dataPath
    self.range = range
    self.bandwidth = bandwidth

  def getData(self): #calls the hackrf_sweep command to get the RF signal data in your area these parms can be explained in the HackRf One Documentaion
    subprocess.call(['hackrf_sweep', '-r', str(self.dataPath), '-f', str(self.range), '-w', str(self.bandwidth), '-1'])
    subprocess.call(['hackrf_spiflash','-R'])

  def sendData(self, rfRange): #send a blank audio file to block a RF signal parms can be explained in the HackRf One Documentaion
    subprocess.call(['hackrf_transfer', '-t', 'testFile2.wav', '-f', str(rfRange), '-p', '1', '-a', '1', '-x', '28', '-s', '1'])

  def csvToJson(self, csvPath, jsonPath): #converts the CSV file the HackRF One produces in the above fintion into a json file
    csvfile = open(str(csvPath), 'r')
    jsonfile = open(str(jsonPath), 'w')
    fieldnames = ("date","time","hz_low","hz_high","bandwidth","samples","DB1","DB2","DB3","DB4","DB5","DB6","DB7","DB8","DB9","DB10","DB11","DB12","DB13","DB14","DB15","DB16","DB17","DB18","DB19","DB20","DB21","DB22","DB23","DB24","DB25","DB26","DB27","DB28","DB29","DB30","DB31","DB32","DB33","DB34","DB35","DB36","DB37","DB38","DB39","DB40","DB41","DB42","DB43","DB44","DB45","DB46","DB47","DB48","DB49","DB50","DB51")
    reader = csv.DictReader(csvfile, fieldnames)
    jsonfile.write('[')
    jsonfile.write('\n')
    First = True
    for row in reader:
      if First == True:
        First = False
      else:
        jsonfile.write(',')
        jsonfile.write('\n')
      json.dump(row, jsonfile)
    jsonfile.write('\n')
    jsonfile.write(']')

  def load(self, jsonPath): #reads in the json file and returns it as an object
    with open(str(jsonPath), 'r') as f:
      distros_dict = json.load(f)
    return distros_dict











