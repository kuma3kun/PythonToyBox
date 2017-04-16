"""
二次元表操作処理テンプレート
"""
class CrossMapCommand:
	SYS_HEAD = "CMC>"
	#処理対象の表データ型
	MAP_TYPE = ""
	#処理対象の表内データ型
	DATA_TYPE = ""
	crossMap = ""

	def __init__(self):
		pass

	def __init__(self ,map, options = None):
		self.crossMap = map

	"""関数の実行"""
	def execute(self):
		#処理
		return map
