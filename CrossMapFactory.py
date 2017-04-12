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
	crossMap = ""
	headFlag = ""

	"""ファイルパスの指定"""
	def __init__(self,path,headFlag = None):
		if headFlag == "0" or headFlag is None :
			print("フラグoff")
			self.headFlag = None
		else :
			self.headFlag = 0

		self.fullPath = path
		self.pathClassify(path)
		self.crossMapping(path)

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

	"""ファイル開いて二次配列にマッピング"""
	def crossMapping(self,path):
		with open(path , mode = "rt" , encoding = "utf-8" ) as file:
			if self.fileExtention == "csv" :
				readFile = pandas.read_csv(file,header = self.headFlag)

			self.crossMap = readFile
				

	def start(self):
		endFlag = 0
		while endFlag == 0 :
			print( self.SYS_HEAD + "コマンド入力してください（list:関数一覧表示 desc:現在の配列確認 write:書き出し end:終了）" )
			command = input(self.SYS_HEAD)

			if command == "desc":
				print(self.crossMap)
			elif command == "end":
				endFlag = 1
			else :
				print(command)



if __name__ == "__main__":
	print("ファイルパスを入力してください")
	inputPath = input()
	print("列名付き？ Yes=1 No=0")
	inputHeadFlag = input()

	obj = CrossMapFactory(inputPath,inputHeadFlag)
	obj.start()


