import csv

#decelerations
scoutOneFile = open("C:\\Users\\Datallite\\Desktop\\python_programs\\scouting_reports\\scout1report.csv","r")
scoutTwoFile  = open("C:\\Users\\Datallite\\Desktop\\python_programs\\scouting_reports\\scout2report.csv","r")
combinedFile = open("C:\\Users\\Datallite\\Desktop\\python_programs\\scouting_reports\\combinedFile.csv","w")


with combinedFile as combinedFile:
    for lines in scoutOneFile:
        combinedFile.write(scoutOneFile.read())
    combinedFile.write("\n")    
    for lines in scoutTwoFile:
        combinedFile.write(scoutTwoFile.read())

with combinedFile as combinedFile:
    dictFile = csv.DictReader(combinedFile.read())
    



