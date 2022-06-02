#Used to find text patterns
import re
patterns = ['term1', 'term2']
text = 'this is a string with term1. Thi another with term3'
print(re.search(patterns[0], text))
print(re.search(patterns[1], text))

for pattern in patterns:
    print('\nSearching for "%s" in:  \n"%s"' %(pattern, text))
    #Checks correspondency
    if re.search(pattern, text):
        print('\n')
        print('Mach was found!\n')
    else:
        print('\n')
        print('No mach was found!\n')

#repeat syntax
#test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dssss...sdddd'
#test_patterns = ['sd*',             #s followed by zero or more d's
#                 'sd+',             #s followed by one or more d's
#                 'sd?',             #s followed by zero or one d
#                 'sd{3}',           #s followed by three d's
#                 'sd{2,3}'          #s followed by two or three d's
#                ]
#multi_re_find(test_patterns,test_phrase)

#StringIO
import io
message = 'this is a normal string'
f = io.StringIO(message)
print(f.read())
print(f.seek(0))
f.close
f = io.StringIO(message)
f.write('. Second line written here.')
print(f.read())
print(f.read())