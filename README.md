# HackRFPiBot
## Using a Raspberry Pi and a HackRF One to locate and graph RF signals on a Python3 Flask Web Server 

###### @authors
- Zachariah L. Henson https://www.linkedin.com/in/zachariah-henson-00a693165/
- Seth French https://www.linkedin.com/in/seth-french-59591017b/

###### @contributors
- Special thanks to the following people for their advising and contributions on this progect.

- Scott Blough- https://www.linkedin.com/in/scottblough
- Dr. Ali Yurekli- https://www.linkedin.com/in/yurekli
- Nicholas Consolo- https://www.linkedin.com/in/nick-consolo-6432227

# IMPORTANT NOTICE
**This project possess the ability to break federal laws and FCC regulations by using this code and reading through this documentation you are agreeing to not use this code/project to break the law and if you chose to use or build this project you understand that all testing must be done in a faraday cage. Visit https://www.fcc.gov/general/jammer-enforcement and https://www.fcc.gov/ for all laws and regulations**

## File Structure
- **Templates/** _contains the html files for the webserver_
- **Static/** _contains all static CDN's and css files **NOTE: The Font Awesome CDN was not included due to size. Independant download required**_
- **Data/**  _contains the .csv and .json file used to store, update, parse, and display the data_
- **Pycache/** _contains the server cache files_
- **In The Parent Directory/**
  1. **Server.py** _The Flask server_
  2. **getHackRFData.py** _The script that interfaces with the HackRf One_
  3. **camera_pi.py** _The script that interfaces with the Pi's camera_
  4. **MISSING** _The audio file used to transmit a signal was ommited due to file size_


## Hardware Used
- HackRf One [HackRf One](https://www.amazon.com/Great-Scott-Gadgets-peripheral-transmission/dp/B01COVX464/ref=sr_1_1_sspa?crid=1FN4F7O1GJSJT&keywords=hackrf+one&qid=1556739808&s=gateway&sprefix=hackrf+one%2Caps%2C152&sr=8-1-spons&psc=1)
- Raspberry Pi 3B+ [RPi](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07BDR5PDW/ref=sr_1_3?crid=2ZMFKANCQR3DQ&keywords=raspberry+pi+3+b%2B&qid=1556739859&s=gateway&sprefix=raspb%2Caps%2C169&sr=8-3)
- High Throughput Cooling Case [Pi Case](https://www.amazon.com/Smraza-Raspberry-Heatsinks-Supply-Black-Clear/dp/B07BT65FT1/ref=sr_1_1_sspa?keywords=raspberry+pi+case&qid=1556740244&s=hi&sr=1-1-spons&psc=1)
- A Good Micro SD Card [SD Card](https://www.amazon.com/Samsung-MicroSD-Adapter-MB-ME32GA-AM/dp/B06XWN9Q99/ref=pd_bxgy_147_img_3/146-7873174-4246317?_encoding=UTF8&pd_rd_i=B06XWN9Q99&pd_rd_r=6bf70053-6c4a-11e9-b1cc-c9dd2e9ccfc7&pd_rd_w=m4afy&pd_rd_wg=A9Jjh&pf_rd_p=a2006322-0bc0-4db9-a08e-d168c18ce6f0&pf_rd_r=6K0DWW6HS49A8NQ5SAYV&psc=1&refRID=6K0DWW6HS49A8NQ5SAYV)
- Mobile Power Supply [Power Supply](https://www.amazon.com/Battery-Pack-Raspberry-4000mAh-Suction/dp/B07BSG7V3J/ref=sr_1_3?keywords=raspberry+pi+3+b%2B+power+pack&qid=1556740353&s=electronics&sr=1-3)
- DC Motor Controler [DC Controler](https://www.amazon.com/gp/product/B01M29YK5U/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
- 4 DC Motors [Pi Motors](https://www.amazon.com/gp/product/B01M29YK5U/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
- DC Power Supply For Motors [DC Power Supply](https://www.amazon.com/LAMPVPATH-Battery-Holder-Switch-Leads/dp/B076C7S2VN/ref=sr_1_6?keywords=dc+motor+power+supply+AA+batteries&qid=1556741377&s=gateway&sr=8-6)
- Simple Robot Frame [Amazon Has Plenty Of Them](https://www.amazon.com/)
- Raspberry Pi Camera [Pi Camera](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_3?crid=1QIIYT6VAP2VU&keywords=raspberry+pi+camera&qid=1556740642&s=electronics&sprefix=raspberry+pi+camer%2Celectronics%2C164&sr=1-3)

## Software/Libraries Used
- Python3 Flask WebServer [Flask](http://flask.pocoo.org/)
- Plotty.js [Plotty](https://plot.ly/javascript/)
- HighCharts.js [HighCharts](https://www.highcharts.com/)
- Font Awesome [FA](https://fontawesome.com/download)
- Custom RPi Camera Script Created By [Ruchir Sharma](https://www.hackster.io/ruchir1674/video-streaming-on-flask-server-using-rpi-ef3d75)
- Pthyon3 csv
- Python3 json
- Python3 subprocess
- Python3 RPi.GPIO
- Python3 RPi.Camera

## Getting Started
- Ensure that your RaspberryPi is updated
```
sudo apt-get update
sudo apt-get upgrade 
```
- Ensure Python3 is installed on the PI
``` sudo python3 ```
  1. If there is an error follow the link to learn how to install python3 [Python3](https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f)
- Install pip3 
``` sudo apt-get install python3-pip ```
- Install Flask
``` sudo pip3 install Flask ```
  1. As a note, you are able to do this within a virtual python environment if you want. The offical Flask documention above shows you how to do that
- Install Flask Bootstrap 
``` pip3 install flask-bootstrap ```
- Install RPi.GPIO 
``` sudo apt-get install python3-rpi.gpio ```
- Install RP.Camera 
``` sudo apt-get install python3-picamera ```
- The rest of the libraries used are CDNs and are included in this repository excluding Font Awesome wich is linked in the Software section
- If you wish to download your own CDNs all the links to download them are next to them in the **Software/Libraries Used** section

## Setting The Raspberry Pi As A Access Point
- This **MUST** be done in order for you to be able to access the webserver in a headless configuration
- Follow this link to learn how to do so [RPi Access Point](https://learn.sparkfun.com/tutorials/setting-up-a-raspberry-pi-3-as-an-access-point/all)
