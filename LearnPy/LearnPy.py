import shutil
import os
import pandas as pd

currentPath = os.getcwd()
dirWithAudio = "log.txt"

data = pd.read_excel('БАЗА АУДИО.xlsx', sheet_name=0)

def getListFromData(nameData):
	isNotNull = pd.notnull(data[nameData])
	items = data.loc[isNotNull,nameData]
	
	items = [str(item).strip().replace("-", "").replace("(", "").replace(")", "").replace(" ", "") for item in items]
	res = []
	for item in items:
		if item.isdigit():
			res.append(item)

	return res

teletel = "Teletel"
ozon = "OZON"
colCetre = "Call-Cetre"
yandexRec = "ЯндексРекрутеры"
yandexKC = "ЯндексКЦ"

result = getListFromData(yandexRec)

def MovePhoneNumbersFromFolder(numbers, nameFolder):
	try:
	    os.mkdir(nameFolder)
	except OSError:
	    print ("Создать директорию %s не удалось" % nameFolder)
	else:
	    print ("Успешно создана директория %s " % nameFolder)
	lines = open(dirWithAudio, 'r').readlines()
	logFileName = "Log File %s.txt" % nameFolder
	logFile = open(logFileName, 'w')
	countLines = len(lines)
	for number in result:
		for line in lines:
			if line.find(number) != -1:
				logFile.write(line)
				newFile = open(currentPath + "\\" + nameFolder + "\\" + number + ".txt", "w")
				newFile.close()
				print(countLines, "\\", countLines , line, end='')
			countLines += 1
	logFile.close()

MovePhoneNumbersFromFolder(getListFromData(yandexRec), "Teletel")