consonants = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']  #finding the consontants of english language 

vowels = ['a', 'e', 'i', 'o', 'u', 'y'] #finding the vowels of english language 
sentence=[]  #create an empty list in order to print all the words you entered 

while True: #keeps running until something stops it 
    word = input("Let's talk some pig latin, insert word: ")  #how to enter input from your keyboard 

    if word[0] in consonants:  #checking the first letter of our word, list slicing 
        cons = (word[1:]+word[0]+"ay") 
        sentence.append(cons) 
        print(cons)
 
    else: 
        vol = (word+"way") 
        sentence.append(vol) 
        print(vol)
 
retry = input("Want to play again? Press ENTER to play or q to quit") 
if retry.lower() == "q": 
    print(sentence) 
    break
