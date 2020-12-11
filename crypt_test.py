import crypt

def test_1passCheck4():
  assert crypt.passCheck4("abcd") == 'abcd', 787

def test_2passCheck4():
  assert crypt.passCheck4("jdti") == 'jdti', 179856

def test_1passCheck5():
  assert crypt.passCheck5("aabbc") == 'aabbc', 759

def test_1passCheckUpper():
  assert crypt.passCheckUpper("jDtI") == 'jDtI', 1344911

def test_1subCip():
  assert crypt.subCipher("_aeioubcdfghjklmnpqrstvwxyz", "hello world", True) == 'cohhlzvlphi'

def test_2subCip():
  assert crypt.subCipher("_aeioubcdfghjklmnpqrstvwxyz", "cohhlzvlphi", False) == 'hello world'
  
def test_3subCip():
  assert crypt.subCipher("_aeiouzyxwvtsrqpnmlkjhgfdbc", "hello world", True) == 'yottqcgqmti'

def test_4subCip():
  assert crypt.subCipher("_aeioubcdfghjklmnpqrstvwxyz", "yottqcgqmti", False) == 'hello world'
