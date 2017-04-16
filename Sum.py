from CrossMapCommand import CrossMapCommand

"""
二次元表操作処理
合計値算出
"""
class Sum(CrossMapCommand) :
	print("あああ")
	SYS_HEAD = "CMC>"
	#処理対象の表データ型
	MAP_TYPE = ""
	#処理対象の表内データ型
	DATA_TYPE = ""
	crossMap = ""

	def __init__(self,map,options = None):
		print("SUM実行")

	"""関数の実行"""
	def execute(self):
		print("SUM関数実行")
		return map

