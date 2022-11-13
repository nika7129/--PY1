from pprint import pprint
di = [{"bin": bin(i), "dec": i,"oct": oct(i),"hex": hex(i)} for i in range(16)]
pprint(di)