# If a word begins with a consonant all consonants before the first vowel are moved to the end of the word and the letters "ay" are then added to the end. e.g. "coin" becomes "oincay" and "flute" becomes "uteflay".
# If a word begins with a vowel then "yay" is added to the end. e.g."egg" becomes "eggyay" and "oak" becomes "oakyay".

# Function to split the letters of a word into a list of lists
def word_split(word):
    return [char.split() for char in word]

# Function to combine a list of lists of letters back into a word, after moving the first letter of the list to the end and append 'ay'
def cons_word_combine(wlist):
    word = ""
    vowels2 = [['a'], ['e'], ['i'], ['o'], ['u'], ['y']]
    holder = []
    keep_running = True
    while keep_running:
        for i in range(len(wlist)):
            if wlist[i] not in vowels2:
                holder += wlist[i]
            elif wlist[i] in vowels2:
                keep_running = False
                break
    llength = len(holder)
    del wlist[0:llength]
    for l in holder:
        wlist.append(list(l))
    for ind in range(len(wlist)):
        for l in wlist[ind]:
            word += l
    return word + 'ay '

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

# # Input prompt + initial processing of input
while True:
    your_input = input("Write a sentence for translation to Pig Latin. Type 'exit' at any time to quit.\n")
    if len(your_input) == 1 and your_input not in vowels:
        print(your_input)
    else:
        split_input = your_input.split()
        if your_input.lower() == 'exit':
            print('Goodbye!')
            break
        sentence = ""
        for thing in split_input:
            if thing[0].lower() not in vowels:
                sentence += cons_word_combine(word_split(thing))
            else:
                sentence += thing+'yay '
        print((sentence.rstrip()))


