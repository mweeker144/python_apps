def magic_reverse(word):
    lst1 = [l for l in word]
    hold = []
    result = ""
    def switcharoo():
        hold.append(lst1.pop())
    i = 0
    while i < len(word):
        i +=1
        switcharoo()
    for x in hold:
        result += str(x)
    return result

while True:
    word = input("Please type a word to reverse. Type 'Exit' at any time to end the program.\n")
    if word.lower() == "exit":
        print('Goodbye!')
        break
    print(magic_reverse(word))


