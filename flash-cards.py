dictionary = {'你好' : 'hello'}
#dictionary = {'hello':'goodbye'};

for c,e in dictionary.items():
    print(c)
    print(e)

print("Please translate");
#zi = input("你阿訇: ")
#print("You entered " + zi)

file = open("test.txt", encoding='utf-8')

dict = {}

for line in file:
    entry = line.split('-')
    assert(len(entry) == 2)
    key = entry[0]
    defn = entry[1]

    dict[key] = defn.strip()

for phrase, defn in dict.items():
    attempt = input(phrase + ': ')
    if attempt.lower() == defn.lower():
        print ("Correct!")
    else:
        print ("Wrong!" + "\t'" + defn + "'");
