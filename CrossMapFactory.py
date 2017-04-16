import re
import importlib
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
	crossMapOrigin = ""
	crossMapAvatar = ""
	headLine = ""
	indexLine = ""

	"""ファイルパスの指定"""
	def __init__(self,path,headLine = None,indexLine = None):
		if headLine == "0" or headLine == "" or headLine is None :
			self.headLine = None
		else :
			self.headLine = 0

		if indexLine == "0" or headLine == "" or indexLine is None :
			self.indexLine = None
		else :
			self.indexLine = 0	

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
		try:
			with open(path , mode = "rt" , encoding = "utf-8" ) as file:
				if self.fileExtention == "csv" :
					readFile = pandas.read_csv(file , header = self.headLine , index_col = self.indexLine )

				self.crossMapOrigin = readFile
				self.crossMapAvatar = readFile
		except IndexError as e:
			print("入力されたファイルは存在しません")
		except IOError as e:
			print("指定されたファイルは開けません")
		else:
			pass
		finally:
			pass
		

	"""登録された関数の実行"""
	def commandCall(self , name , options = None):
		print(name)
		print(options)
		try:
			mod = importlib.import_module(name)
			commandClass = getattr(mod,name)
			print(commandClass)
			commandObj = commandClass(self.crossMapOrigin , options = None)
			print(type(commandObj))
			commandObj.execute()
		except ModuleNotFoundError as e:
			print("入力されたコマンドは存在しません")
		else:
			pass
		finally:
			pass

	def commandHelp(self, options = None):
		mod = __import__("CrossMapCommand")
		subclasses = mod.__subclasses__()
		print(subclasses)
				
	"""CUI操作用"""
	def start(self):
		endFlag = 0
		while endFlag == 0 :
			print( self.SYS_HEAD + "コマンド入力してください（list:関数一覧表示 desc:現在の配列確認 write:書き出し end:終了）" )
			command = input(self.SYS_HEAD)

			if command == "desc":
				print(self.crossMapOrigin)
			elif command == "end":
				endFlag = 1
			elif command == "help":
				self.commandHelp()
			elif command != "":
				itr = command.split(" ")
				commandName = itr.pop(0)
				options = []
				for i in itr:
					options.append(i)				
				self.commandCall( commandName , options )
			else :
				print(command)



if __name__ == "__main__":
	print("ファイルパスを入力してください")
	inputPath = input()
	print("列名付き？ Yes=1 No=0")
	inputHeadLine = input()
	print("行番号付き？ Yes=1 No=0")
	inputIndexLine = input()

	obj = CrossMapFactory(inputPath,inputHeadLine,inputIndexLine)
	obj.start()


