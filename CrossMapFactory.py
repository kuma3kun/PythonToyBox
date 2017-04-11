import re
import pandas

"""
二次元表操作用クラス
"""
class CrossMapFactory:
	SYS_HEAD = "CrMp>"
	fullPath = ""
	filePath = ""
	fileName = ""
	fileExtention = ""
	crossMap = []

	"""パスの分類"""
	def pathClassify(self,path):
		lead = re.search("^.",path)

		if lead == "." or lead == "/":
			#フルパス分解 path:パス name:ファイル名 extention:拡張子
			pathSplit = re.search("(?P<path>^.*\/)(?P<name>.*?)\.(?P<extention>.*$)",path)
			self.filePath = pathSplit.group("path")
			self.fileName = pathSplit.group("name")
			self.fileExtention = pathSplit.group("extention")
		else:
			#ファイル名分解 name:ファイル名 extention
			pathSplit = re.search("(?P<name>.*?)\.(?P<extention>.*$)",path)
			self.fileName = pathSplit.group("name")
			self.fileExtention = pathSplit.group("extention")

	"""ファイルパスの指定"""
	def __init__(self,path):
		self.fullPath = path
		self.pathClassify(path)
		self.crossMapping(path)

	"""ファイル開いて二次配列にマッピング"""
	def crossMapping(self,path):
		with open(path , mode = "rt" , encoding = "utf-8" ) as file:
			print(file)
			if self.fileExtention == "csv" :
				readFile = pandas.read_csv(file)
				print(type(readFile))
				print(readFile)

			rowCount = 0
			for row in readFile:
				self.crossMap[rowCount].append(row)
			print(self.crossMap)
				

	def start(self):
		endFlag = 0
		while endFlag == 0 :
			print( self.SYS_HEAD + "コマンド入力してください（list:関数一覧表示 desc:現在の配列確認 write:書き出し end:終了）" )
			command = input(self.SYS_HEAD)

			if command == "desc":
				print(self.crossMap)
			elif command == "end":
				endFlag = 1



if __name__ == "__main__":
	print("ファイルパスを入力してください")
	inputPath = input()

	obj = CrossMapFactory(inputPath)
	obj.start()


