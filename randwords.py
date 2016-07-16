import wordfreq,string,random
filter = ""
for c in string.punctuation:
	if c != "'":
		filter += c
def getListFreqDict(list):
	ret = wordfreq.getFreqDict(" ".join(list),filterchars=filter)
	return ret
def getRandomWords(freqDict):
	t = ""
	for s in freqDict:
		t += "{} ".format(s) * freqDict[s]
	listW = [x for x in t.split(" ") if x != ""]
	len = random.randint(1,20)
	ret = ""
	while len != 0:
		ret += random.choice(listW)
		ret += " "
		len -= 1
	return ret[:-1]+random.choice(".!?;")
