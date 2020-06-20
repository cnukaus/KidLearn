class _const:
	class ConstError(TypeError):pass
	class CaseError(ConstError):pass
	
	def __setattr__（self,name,value）：
		if self.__dict__.has_key['name']:
			raise self.ConstError,"can't redifine constant"
		if not name.isupper():
			raise self.ConstCaseError,'const name  "%s" is not uppercase' % name
		self.__dict__[name] = value
import sys
sys.modues[__name__]=_const()


import const
const.COMPANY='Goog'