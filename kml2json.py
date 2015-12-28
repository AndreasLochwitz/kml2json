from xml.dom.minidom import parse
import json
import sys   

__author__ = "Andreas Lochwitz"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "andreas_lochwitz(at)live.de"

def getPlaceMarks(dom):
    return dom.getElementsByTagName("Placemark")

def getPlaceMarkName(placemark):
    return placemark.getElementsByTagName("name")[0].childNodes[0].data
    
def getPlaceMarkCoordinates(placemark):
    coordinates = placemark.getElementsByTagName("coordinates")[0].childNodes[0].data
    coordArray = coordinates.split(",")
    return { 'latitude': coordArray[1], 'longitude': coordArray[0] }
    
def writeJsonFile(jsonData, jsonFileName):
    print("Writing JSON to file " + jsonFileName)
    f = open(jsonFileName, 'w')
    f.write(jsonData)
    f.close()

def processFile(inFileName, outFileName):
    dom = parse(inFileName)
    placemarks = getPlaceMarks(dom)
    print("Found " + str(len(placemarks)) + " placemarks in file " + inFileName )
    resultData = []
    for placemark in placemarks:
        placeMarkName = getPlaceMarkName(placemark)
        placeMarkData = getPlaceMarkCoordinates(placemark)
        placeMarkData['name'] = placeMarkName
        resultData.append(placeMarkData)
    jsonData = (json.dumps(resultData, sort_keys=True, indent=2))
    writeJsonFile(jsonData, outFileName)                

def main():
    if (len(sys.argv) == 3):
        inFile = sys.argv[1]
        outFile = sys.argv[2]
        processFile(inFile, outFile)
    else:
        print("Wrong number of parameters\nExample: python kml2json.py source.kml target.json")

main()
