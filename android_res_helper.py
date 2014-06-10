from translate import Translator
import os

lang_list = ["de", "es", "fr", "it", "nl", "pl", "pt"]

# resource filename for translate
fileToTraslate = 'str.xml'

# result filename after translate
destFile = 'gms_strings.xml'

startLine = '<string name='
endLine = '</string>'

lines = [line.strip() for line in open(fileToTraslate)]

for lang in lang_list:
	directory = "values-" + lang
	if not os.path.exists(directory):
		os.makedirs(directory)

	destF = open(directory + "/" + destFile, "w")
	for s in lines:
		if(startLine in s):
			idxStart = s.index('">') + 2
			idxEnd = s.index(endLine)
			transWord = s[idxStart:idxEnd]
			translator= Translator(to_lang=lang)
			resultWord = translator.translate(transWord).encode('utf-8')
			newStr = s[:idxStart] + resultWord + endLine
			destF.write("%s\n" % newStr)
		else:
			destF.write("%s\n" % s)
