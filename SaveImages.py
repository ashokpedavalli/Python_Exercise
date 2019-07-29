import ConfigParser
import os
import urllib
import urllib2

try:
    inputTxtFilePath = raw_input("Enter the name of text file : ")
    iniFileConfig = r".\FILE.INI"
    config = ConfigParser.ConfigParser()
    config.read(iniFileConfig)
    outImageSavePath = config.get("Destination", "ImagesPath")
    # Check path
    if os.path.exists(inputTxtFilePath):
            if not os.path.exists(outImageSavePath):
            # If the folder is not exit, create a folder
                os.mkdir(outImageSavePath)
            # Open text file and iterate the loop
            inputText = open(inputTxtFilePath, "r")
            for eachURL in inputText:
                # Check URL is valid or not
                try:
                    checkConn = urllib2.urlopen(eachURL)
                except:
                    message = "Invalid Image URL, Please check : " + inputTxtFilePath
                    raise
                if checkConn.code == 200:
                    # Download image
                    checkConn.close()
                    outImagePath = os.path.join(outImageSavePath, eachURL.split('/')[len(eachURL.split('/'))-1])
                    if not os.path.isfile(outImagePath.strip()):
                        # Download the new file
                        urllib.urlretrieve(eachURL, outImagePath.strip())
                    else:
                        # If file is existed then replace with new file (based on requirment we can change logic for replace/delete files)
                        urllib.urlretrieve(eachURL, outImagePath.strip())
                else:
                    print("URL Not exist")
    else:
        print("Given " + inputTxtFilePath + " is not a valid path.")
    print("Process Completed Successfully")
except:
    print(message)
