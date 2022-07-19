import csv

#decelerations
scoutOneFile = open("scout1report.csv","r")
scoutTwoFile  = open("scout2report.csv","r")
combinedFile = open("combinedFile.csv","w")


with combinedFile as combinedFile:
    for lines in scoutOneFile:
        combinedFile.write(scoutOneFile.read())
    combinedFile.write("\n")    
    for lines in scoutTwoFile:
        combinedFile.write(scoutTwoFile.read())
    



