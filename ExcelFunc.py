import sys
import csv 
import re

def clannad(crossMap):
	okazaki = "岡崎最高！"
	benza = "それと便座カバー"
	rowNum = 0
	resultMap = []

	for row in crossMap:
		if not( rowNum == 0 ):
			if row[1] == "" :
				row[1] = okazaki
			else :
				row[2] = benza
		resultMap.append(row)
		rowNum = rowNum + 1

	return resultMap


if __name__ == "__main__" :

	print("csvファイルのフルパス入力してね")
	inputPath = input()

	#ファイル読み込み（パス,読み込みモード=テキスト読み込み,エンコード=UTF-8）
	with open(inputPath,mode = "rt",encoding="utf-8") as excelFile:
		#フルパス分解
		#\1 パス
		#\2 ファイル名
		#\3 拡張子
		pathSplit = re.search("(?P<Path>^.*\/)(?P<name>.*?)\.(?P<extension>.*$)",inputPath)
		#pathSplit = re.search("(?P<name>.*?)\.(?P<extension>.*$)",inputPath)
		extension =  pathSplit.group(3)

		if extension == "csv":
			excelRender = csv.reader(excelFile)
		
		crossMap = []

		#先頭行飛ばし
		header = next(excelRender)
		crossMap.append(header)

		#CSV行数繰り返し
		for row in excelRender:
			#print(row)
			crossMap.append(row)

		print(crossMap)

		print(clannad(crossMap))

	print(extension)

	input()


