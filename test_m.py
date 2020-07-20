#!/usr/bin/env python
#
# Copyright (c) 2013 Pavol Rusnak
# Copyright (c) 2017 mruddy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from __future__ import print_function

import json
import random
import sys
import unittest
from binascii import hexlify, unhexlify

from mnemonic import Mnemonic

#https://realpython.com/python-testing/#unit-tests-vs-integration-tests
class MnemonicTest():
    def my_9thfun(self):
        print(sum([1,1]) == 3)
    def _check_list(self, language, vectors):
        mnemo = Mnemonic(language)
        for v in vectors:
            code = mnemo.to_mnemonic(unhexlify(v[0]))
            seed = hexlify(Mnemonic.to_seed(code, passphrase="TREZOR"))
            xprv = Mnemonic.to_hd_master_key(unhexlify(seed))
            if sys.version >= "3":
                seed = seed.decode("utf8")
            #self.assertIs(mnemo.check(v[1]), True)
            print(v[1] == code)
            print(v[2] == seed)
            print(v[3] == xprv)
    def test_vectors(self):
        with open("vectors.json", "r") as f:
            vectors = json.load(f)
        for lang in vectors.keys():
            self._check_list(lang, vectors[lang])

    


def __main__():
    m=MnemonicTest()
    m.my_9thfun()
    m.test_vectors()


if __name__ == "__main__":
    __main__()
    
