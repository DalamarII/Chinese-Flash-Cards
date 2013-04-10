dictionary = {'你好' : 'hello'}
#dictionary = {'hello':'goodbye'};

for c,e in dictionary.items():
    print(c)
    print(e)

print("Please translate");
#zi = input("你阿訇: ")
#print("You entered " + zi)

# some sort of enum magic found here:
# http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

PhraseType = enum('Noun', 'Verb', 'Adjective')

file = open("definitions.txt", encoding='utf-8')

dict = {}

for line in file:
    entry = line.split('-')
    assert(len(entry) == 2)
    key = entry[0]
    defn = entry[1]

    dict[key] = defn.strip()

i = 1
for phrase, defn in dict.items():
    if (i > 20):
        break
    attempt = input(str(i) + ')' + phrase + ': ')
    i = i+1

    # TODO: Not 100% sure but I think for loops go in order in lists
    # This means we can rely on this sequential parsing of the loop
    # to check for the presence or absence of phrase types
    defnList = defn.split('/')

    numDefn = len(defnList)
    numCorrect = 0

    # Sort word type

    for d in defnList:
        if attempt.lower() == d.lower():
            numCorrect = numCorrect + 1

    if numCorrect > 0:
        print("\tCorrect!")
        if numCorrect < numDefn:
            print ("\tAlso means '" + defn + "'")
    else:
        print ("\tWrong!" + "\t'" + defn + "'");
