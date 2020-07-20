# to use c? Pickle loader

import unittest
import time
from mnemonic import Mnemonic
import random
import binascii
import hashlib

class testcase(unittest.TestCase):
	def test1(self):
		self.assertEqual(sum([1,1]),2,"Equal")

	def read_dict(self,n):
		count=0
		for a in open("BIP039.txt"):
			count = count +1
			if count>n:
				break
			self.assertIn("ab",a )

	def gen_list(self,n):
		count = 0
		full = open("BIP039.txt").read().splitlines()   
		leng = len(full)
		value = []
		for i in range(0,n):
				value.append(random.choice(full))
		print("value:",value)
		return value



# https://ethereum.stackexchange.com/questions/72815/convert-bip-39-mnemonic-to-ethereum-private-key-in-python
#https://github.com/vergl4s/ethereum-mnemonic-utils
#https://iancoleman.io/bip39/#english
# test here: https://iancoleman.io/bip39/#english 
	def combine(self,list1,list2,seq1,seq2):
		result = [None] * (len(seq1) +len(seq2))
		
		count = 0
		 # convert Actual sequence - start from 1, to Python list seq [start from 0]
		for word in list1:
			i = seq1[count] -1
			result[i]=word
			count += 1
			
		count = 0
		for word in list2:
			i = seq2[count] -1
			result[i]=word
			count += 1
		
		


		return result

	def read_incomplete(self,incomplete_list,total_count,seq):
		
		global complete
		valid_incomplete = 0
		missing = list(set(range(1,seq[-1])) - set(seq))

		

		full = open("BIP039.txt").read().splitlines()
		
		for word in incomplete_list:
			#self.assertIn(word,full)
			if word in full:
				valid_incomplete += 1
				full.remove(word)

		extra = total_count - valid_incomplete
		print("extra words:",extra)
		
		matched = False
		while not matched:


			extra_list = []
			full_copy=full.copy()
			#print("iter:",len(full_copy),"full:",len(full),"extra ",extra)
			
			for i in range(0,extra):
				# non repeating pick
				if len(full_copy) >= extra:
					pick=random.choice(full_copy)
					extra_list.append(pick)
					full_copy.remove(pick)
					
				else:
					break
				#print(full_copy)

			result = self.combine(incomplete_list,extra_list,seq,missing)
			if complete  == result:
				matched = True

			#print(matched)
			

		return extra_list


test1=testcase()

m = Mnemonic("english")
complete="episode image leaf staff pitch raise evil comic bicycle author crop dentist"#.split(" ")

#to_seed
complete=m.normalize_string(complete).encode("utf-8")

passphrase = "TREZOR".encode("utf-8")
PBKDF2_ROUNDS = 2048

stretched = hashlib.pbkdf2_hmac("sha512", complete, passphrase, PBKDF2_ROUNDS)
print("stretch",binascii.hexlify(stretched[:64]),"len:",len(binascii.hexlify(stretched[:64])))
print("key:",m.to_hd_master_key(binascii.unhexlify(binascii.hexlify(stretched[:64]))))


complete=['enrich', 'already', 'purse', 'escape', 'gift', 'album' ,'adjust']
incomp=['enrich', 'already', 'purse', 'escape',  'adjust'] # say we need CAOGO btw GIft and Adjust

seq=[1,2,3,4,7]  #


print (test1.combine(incomp,['ookk'],seq, list(set(range(1,seq[-1])) - set(seq))))
#incomplete_list = list( set (incomplete_list))
start = time.time()

#data=binascii.unhexlify(test1.gen_list(16))
print("found",test1.read_incomplete(incomp,7,seq))  #incomp.split(",")

end = time.time()
print("time used:",end - start)

data="".join(test1.gen_list(16))
print(m.to_seed(data))

#to_mnemonic is from number to words, assertEqual(m.to_entropy(m.to_mnemonic(d).split()), d)

imcomplete=""

if __name__== '__main__':
	#test1.read_dict(5)
	
	unittest.main()
	
	data=read_incomplete(self,incomplete_list,total_count)
	
'''Data length should be one of the following: [16, 20, 24, 28, 32], but it is not (12).'''
# if len(mnemonic) not in [12, 15, 18, 21, 24]:
