# import stuff
import os, random

# update this to be your movie directory
movieDir ='D:\Share\Movies'

# name of file that stores your movies
movieListFile = "movieList.txt"

# extenions for movie files
exts = [".avi",".flv",".wmv",".mov",".mp4",".mkv"]

# scan all the files to make a list of all the movies
def getMovieList():
    movieList = open(movieListFile, "w")
    for subdir, dirs, files in os.walk(movieDir):
        for file in files:
            thisFile = os.path.join(subdir, file)

            hiddenMacFile = False

            # filter out the hidden mac files
            if "\." in thisFile:
                hiddenMacFile = True
                # do nothing

            if hiddenMacFile == False:
                for ext in exts:
                    if ext in thisFile:
                        movieList.write(thisFile + "\n")
                        # print(thisFile)
    movieList.close()

# get a random movie from the movieListFile
def getRandomMovie():
    movieList = open(movieListFile, "r")

    allLines = movieList.readlines()
    # print(allLines[0])

    randomNum = random.randint(0, len(allLines) - 1)

    # print("randomNum:" + str(randomNum))
    # print("RandomMove: " + allLines[randomNum])

    movieList.close()
    return allLines[randomNum][:-1]

getMovieList()
randomMovie = getRandomMovie()

answer = "N"

# keep asking question ...until Yes
while answer != "Y" and answer != "y" and answer != "Yes" and answer != "yes":
    answer = input("Would you like to watch \n " + randomMovie + "\n(Y/N) ?")
    if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes":
        os.startfile(randomMovie)
        print("**enjoy your Movie**")
    else:
        # get another random movie!
        randomMovie = getRandomMovie()
