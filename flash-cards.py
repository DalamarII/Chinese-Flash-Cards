dictionary = {'你好' : 'hello'}
#dictionary = {'hello':'goodbye'};

for c,e in dictionary.items():
    print(c)
    print(e)

print("Please translate");
#zi = input("你阿訇: ")
#print("You entered " + zi)

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
    if attempt.lower() == defn.lower():
        print ("\tCorrect!")
    else:
        print ("\tWrong!" + "\t'" + defn + "'");
