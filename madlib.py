import re 

import pyinputplus as pyip 

wordsToReplace = re.compile(r'''((NOUN)|(VERB)|(ADJECTIVE)|(ADVERB))''')

madlibTextFileInput = open(r'madlib.txt','r')
output = ''
lines = madlibTextFileInput.readlines()
madlibTextFileOutput = open(f'madlibresult.txt','w')


for line in lines :
    

    for words in wordsToReplace.findall(line):
        userInput = pyip.inputStr('Enter an %s :\n' %(words[0].lower()) )
        line = line.replace(words[0],userInput,1)
    madlibTextFileOutput.writelines(line)
    output += line

print(output)