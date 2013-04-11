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

class DefinitionEntry:
    ''' A definition entry in the Chinese to English dictionary.
 It's simply a convenient way of grouping together phrase type and phrase. '''
    def __init__(self, type, phrase):
        self.type = type
        self.phrase = phrase

    def __str__(self):
        return self.type + '. ' + self.phrase

PhraseType = enum(Noun = 'n', Verb = 'v', Adjective = 'adj', Idiom =  'i')

file = open("definitions.txt", encoding='utf-8')

dict = {}

for line in file:
    entry = line.split('-')
    assert(len(entry) == 2)
    key = entry[0]
    english = entry[1]

    # Create a list of DefinitionEntrys
    englishList = english.strip().split('/')

    defnList = []
    type = 0

    # TODO: Not 100% sure but I think for loops go in order in lists
    # This means we can rely on this sequential parsing of the loop
    # to check for the presence or absence of phrase types
    for d in englishList:
        dList = d.split('.', 1)
        if len(dList) > 1:
            assert(len(dList) == 2)
            type = dList[0]
            phrase = dList[1].strip()
        else:
            phrase = dList[0].strip()

        defnList.append(DefinitionEntry(type, phrase))
    	    
    dict[key] = defnList

i = 1
for phrase, defn in dict.items():
    if (i > 20):
        break
    attempt = input(str(i) + ')' + phrase + ': ')
    i = i+1

    numDefn = len(defn)
    numCorrect = 0

    # Sort word type
    for d in defn:
        if attempt.lower() == d.phrase.lower():
            numCorrect = numCorrect + 1

    if numCorrect > 0:
        print("\tCorrect!")
        if numCorrect < numDefn:
            print ("\tAlso means:")
            for d in defn:
                print('\t' + str(d))
    else:
        print ("\tWrong!");
        for d in defn:
            print('\t' + str(d))
