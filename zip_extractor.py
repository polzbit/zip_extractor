#!/usr/bin/python3

import os
from zipfile import ZipFile
from argparse import ArgumentParser

def getParse():
    # setup arguments
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', help='Enter path to INPUT folder, contains zip files.')
    parser.add_argument('-o', '--output', dest='output', help='Enter path to OUTPUT folder, extract zip files to this folder.')
    # check arguments
    arguments = parser.parse_args()
    if not arguments.input:
        parser.error('[!] Specify INPUT folder --help for more information')
    else:
        inpath = arguments.input
        outpath = arguments.output
        if not arguments.output:
            outpath = arguments.input
        files = extractFiles(inpath, outpath)
        if not len(files):
            parser.error("[!] Couldn't find zip files on given path")
        else:
            print('Files extracted successfuly to ' + outpath)

# get all files in folder recursively, files that end with one of the ext tuple arguments
def getListOfFiles(dirName, ext):
        # create a list of file and sub directories 
        # names in the given directory 
        listOfFile = os.listdir(dirName)
        allFiles = list()
        
        # Iterate over all the entries
        for entry in listOfFile:
            # check file extention
            if entry.endswith(ext):
                # Create full path
                fullPath = os.path.join(dirName, entry)
                # If entry is a directory then get the list of files in this directory 
                if os.path.isdir(fullPath):
                    allFiles = allFiles + getListOfFiles(fullPath, ext)
                else:
                    allFiles.append(fullPath)
                    
        return allFiles

# extract zip files in path
def extractFiles(inDir, outDir):
    all_files = getListOfFiles(inDir, (".zip"))
    for f in all_files:
        with ZipFile(f, 'r') as zip_ref:
            zip_ref.extractall(outDir)
    return all_files

if __name__ == "__main__":
    getParse()

