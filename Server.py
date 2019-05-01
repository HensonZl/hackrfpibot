#@authors Zachariah L Henson and Seth French and copyrighted under the MIT lience
from flask import Flask, render_template, Response #the framework for the webserver
from flask_bootstrap import Bootstrap #a js libary for css, js and html
import datetime #the date is important
import RPi.GPIO as gpio #allows for the use of GPIO pins on the raspberry pi
import time #for time stamps
import json #json is the file format we used to minipulate the data
from flask.json import jsonify #allows for the use of json in the webserver as a response to a $.get commoand is js
from camera_pi import Camera # a script that allows for the brodcast of the camera interface on the website
from getHackRFData import HackRF # a custom stript that interfaces with the hackrf one

app = Flask(__name__) #init the web app
Bootstrap(app) #let the ap know you will use bootstrap framework
app.config['BOOTSTRAP_SERVE_LOCAL'] = True #the location for the static CDN of the bootstrap

gpio.setmode(gpio.BCM) #setting the gpio mode on the pi to be able to access them
gpio.setwarnings(False) #no need for warnings after development change to true if you need the warnings

dcOne = 17 #sets the gpio pin number to a var for future use
dcTwo = 22
dcThree = 23
dcFour = 24

gpio.setup(dcOne,gpio.OUT) #setts the mode of the gpio pin to know it will be recieving info to send out
gpio.setup(dcTwo,gpio.OUT)
gpio.setup(dcThree,gpio.OUT)
gpio.setup(dcFour,gpio.OUT)

gpio.output(dcOne,gpio.LOW) # turn all of the gpio pins off, we dont need a run away robot
gpio.output(dcTwo,gpio.LOW)
gpio.output(dcThree,gpio.LOW)
gpio.output(dcFour,gpio.LOW)



@app.route("/") #home dir of the webserver
def index():

   templateData = { #if we needed to return data it would be done here

      }

   return render_template('index.html', **templateData) #return the template of the website in html format for the user to see

def gen(camera): #define the camera function to be used 

    """Video streaming generator function."""

    while True:

        frame = camera.get_frame() #gets the current frame of the cammera from the script

        yield (b'--frame\r\n'

               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') #sets the display format

@app.route('/video_feed') #dir of the camera interface
def video_feed():

    """Video streaming route. Put this in the src attribute of an img tag."""

    return Response(gen(Camera()), #displays the current frame of the camera to the /video_feed dir

                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/gengraph/<range>') #the dir were all the HackRF data is collected and formated and accepts a parm that allows for the user to choose a rf signal range
def gengraph(range):
  RfRange = str(range) #converts the user input into a usable string
  HRF = HackRF("/home/pi/Documents/rpiWebServer/data/dataRaw.csv", RfRange, "100000") #3 parms. location of were to dump the CSV data, the range to scan and how many MHz between each hop, currently .1 Mhz

  HRF.getData() #calls the fuction to get the data from the HackRF with the above parms

  HRF.csvToJson("/home/pi/Documents/rpiWebServer/data/dataRaw.csv", "/home/pi/Documents/rpiWebServer/data/dataJ.json") #calls a function to convert the data from CSV to JSON with the file paths as parms

  jobj = HRF.load("/home/pi/Documents/rpiWebServer/data/dataJ.json") # calls a funtion that loads the JSON data into a object

  def extract_time(json):

    try:

        # Also convert to int since update_time will be string.  When comparing

        # strings, "10" is smaller than "2".

        return int(json['hz_low'])

    except KeyError:

        return 0
  
  jobj.sort(key=extract_time, reverse=False) #sorts the json data to be ordered correctly

  y_cords = [] #y cords object
  x_cords = [] #x cords object

  bandwidth = 98039.22 #the exact MHz between hops in the scans
  spacer = 49019.61 #used to find the middle of the signal
  startingHz = 0.0 #sets a starting point

  for distro in jobj: #sets all of the y cords from the json object

    y_cords.append((float(distro['DB1'])))
    y_cords.append((float(distro['DB2'])))
    y_cords.append((float(distro['DB3'])))
    y_cords.append((float(distro['DB4'])))
    y_cords.append((float(distro['DB5'])))
    y_cords.append((float(distro['DB6'])))
    y_cords.append((float(distro['DB7'])))
    y_cords.append((float(distro['DB8'])))
    y_cords.append((float(distro['DB9'])))
    y_cords.append((float(distro['DB10'])))
    y_cords.append((float(distro['DB11'])))
    y_cords.append((float(distro['DB12'])))
    y_cords.append((float(distro['DB13'])))
    y_cords.append((float(distro['DB14'])))
    y_cords.append((float(distro['DB15'])))
    y_cords.append((float(distro['DB16'])))
    y_cords.append((float(distro['DB17'])))
    y_cords.append((float(distro['DB18'])))
    y_cords.append((float(distro['DB19'])))
    y_cords.append((float(distro['DB20'])))
    y_cords.append((float(distro['DB21'])))
    y_cords.append((float(distro['DB22'])))
    y_cords.append((float(distro['DB23'])))
    y_cords.append((float(distro['DB24'])))
    y_cords.append((float(distro['DB25'])))
    y_cords.append((float(distro['DB26'])))
    y_cords.append((float(distro['DB27'])))
    y_cords.append((float(distro['DB28'])))
    y_cords.append((float(distro['DB29'])))
    y_cords.append((float(distro['DB30'])))
    y_cords.append((float(distro['DB31'])))
    y_cords.append((float(distro['DB32'])))
    y_cords.append((float(distro['DB33'])))
    y_cords.append((float(distro['DB34'])))
    y_cords.append((float(distro['DB35'])))
    y_cords.append((float(distro['DB36'])))
    y_cords.append((float(distro['DB37'])))
    y_cords.append((float(distro['DB38'])))
    y_cords.append((float(distro['DB39'])))
    y_cords.append((float(distro['DB40'])))
    y_cords.append((float(distro['DB41'])))
    y_cords.append((float(distro['DB42'])))
    y_cords.append((float(distro['DB43'])))
    y_cords.append((float(distro['DB44'])))
    y_cords.append((float(distro['DB45'])))
    y_cords.append((float(distro['DB46'])))
    y_cords.append((float(distro['DB47'])))
    y_cords.append((float(distro['DB48'])))
    y_cords.append((float(distro['DB49'])))
    y_cords.append((float(distro['DB50'])))
    y_cords.append((float(distro['DB51'])))

  for distro in jobj: #sets all of the x cords for the RF signals based on the space between hops and the middle of the signal. as a note rf singals are read from the middle of the signal not the begining so thats why it is formated like this
    startingHz = float(distro['hz_low'])
    startingHz += spacer
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
    startingHz += bandwidth
    x_cords.append(startingHz)
  
  cords = [x_cords,y_cords] #puts the x and y cords in a parent object

  return jsonify(cords) #returns the parent object to the client 

@app.route('/block/<blockRange>') #warrning do not use this function outside of a fareaday cage as it is breaks FCC regulations
def block(blockRange): #blocks a rf sgnial range
  RfRange = str(blockRange) #formats the user input into a string
  HRF = HackRF("/home/pi/Documents/rpiWebServer/data/dataRaw.csv", RfRange, "100000") #init the HackRF
  HRF.sendData(RfRange) #calls a funtion to block a RF signal based on the user input

  randomData = ['hello', 'hello'] #you need to return data for a funtion to be called by $.get in a flask server

  return jsonify(randomData) # read the above comment


@app.route("/<deviceName>/<action>") #the dir that controls the robot
def action(deviceName, action):
	if deviceName == 'robot': #inits the gpio pins read the code at the beggining of the file to understand better
		actuator1 = dcOne
		actuator2 = dcTwo
		actuator3 = dcThree
		actuator4 = dcFour

	if action == "backwards": #sets the pins to go a direction based on user input
		gpio.output(actuator1, False)
		gpio.output(actuator2, True)
		gpio.output(actuator3, False)
		gpio.output(actuator4, True)

	if action == "forwards": #sets the pins to go a direction based on user input
		gpio.output(actuator1, True)
		gpio.output(actuator2, False)
		gpio.output(actuator3, True)
		gpio.output(actuator4, False)

	if action == "left": #sets the pins to go a direction based on user input
		gpio.output(actuator1, False)
		gpio.output(actuator2, True)
		gpio.output(actuator3, True)
		gpio.output(actuator4, False)

	if action == "right": #sets the pins to go a direction based on user input
		gpio.output(actuator1, True)
		gpio.output(actuator2, False)
		gpio.output(actuator3, False)
		gpio.output(actuator4, True)
	
	if action == "off": #sets the pins to go a direction based on user input
		gpio.output(actuator1, gpio.LOW)
		gpio.output(actuator2, gpio.LOW)
		gpio.output(actuator3, gpio.LOW)
		gpio.output(actuator4, gpio.LOW)
	
	templateData = {

              }

	return jsonify(templateData) #agian you have to return something in a fuction



if __name__ == "__main__":

   app.run(host='0.0.0.0', port=80, debug=True, threaded=True) #starts the app on a port on the local host
