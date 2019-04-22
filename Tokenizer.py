import re
words = open("mergedTokens.en" , "r")
test = open("en.tokens.en" , "r")
test_line = len(open("en.tokens.en").readlines(  ))


letter = []
exetoken = []
result = []


for i in range(0,1000):

    wordline = words.readline()
    print(wordline)
    wordes = re.sub('\n', "", wordline)
    tokenen = str(i+1) + "."  + wordes + ' => '
    result.append(tokenen)
    for ch in wordes:
        letter += ch
    letwor = letter
    cword = ''.join(map(str, letter))
    cleanword = ''.join(map(str, letter))

    for j in range(0, len(letter)+1 ):
        for w in range(0,len(letter)+1):


            for q in range(0, test_line):
                token = test.readline()
                token = re.sub('\n', "", token)
                cleanword = ''.join(map(str, cword[w:]))

                if(cleanword == token):

                    exetoken.append(cleanword)
                    cword = re.sub(cleanword, "", cword)



            test.close()
            test = open("en.tokens.en", "r")
    lentoken = len(exetoken)-1

    while(lentoken >= 0):
        result.append(exetoken[lentoken])
        result.append(" ")
        lentoken = lentoken - 1

    res = ''.join(map(str, result))
    print(res)
    with open('exec.txt', 'a') as the_file:
        the_file.write(res+'\n')
    result.clear()
    exetoken.clear()
    letter.clear()

