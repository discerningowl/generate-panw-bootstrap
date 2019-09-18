#!/usr/bin/python

import os

def ReadInputFile(fn):
    #Read the input file and store as a list
    try:
      with open(fn) as f:
        fwList = f.read().splitlines()
      return fwList
    except IOError:
      print "Error: File does not appear to exist."
      return 0

def MakeDirStructure(mds):
    #Create the necessary directory structure for PANW Bootstrapping
    try:
        for item in mds:
            configPath = os.path.join(item, 'config')
            contentPath = os.path.join(item, 'content')
            licensePath = os.path.join(item, 'license')
            softwarePath = os.path.join(item, 'software')
            os.makedirs(configPath)
            os.makedirs(contentPath)
            os.makedirs(licensePath)
            os.makedirs(softwarePath)

    except IOError:
      print "Error: File does not appear to exist."
      return 0

def MakeInitCfg(rn):
    # Read in the templatized init-cfg-template file, replace the variables
    # Write out to new file under the firewall's new directory
    try:
        for item in rn:
            # Open template init-cfg-template file
            with open('init-cfg-template.txt', 'r') as startFile :
                filedata = startFile.read()

            # Replace the target string
            filedata = filedata.replace('%name%', item)

            # Set path for init-cfg.txt file
            dirPath = os.path.join(item, 'config')

            # Write the file out in proper directory
            with open(os.path.join(dirPath, 'init-cfg.txt'), 'w') as endFile:
                endFile.write(filedata)
    except IOError:
        print "Error: Cannot create init-cfg.txt file."
        return 0

def MakeAuthCode(mac):
    try:
        for item in mac:
            # Open the authcodes-template file
            with open('authcodes-template.txt', 'r') as origFile :
                filedata = origFile.read()

            # Set path for authcodes file
            dirPath = os.path.join(item, 'license')

            # Write the file out in proper directory
            with open(os.path.join(dirPath, 'authcodes'), 'w') as finalFile:
                finalFile.write(filedata)
    except IOError:
        print "Error: Cannot create init-cfg.txt file."
        return 0

resultNames = ReadInputFile("vars.text")
MakeDirStructure(resultNames)
MakeInitCfg(resultNames)
MakeAuthCode(resultNames)
