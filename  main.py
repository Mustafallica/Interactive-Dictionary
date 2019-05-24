# Mustafa AL-Jaburi

import json
from difflib import get_close_matches

#loading,openning and storing json in data. 
data = json.load(open("data.json")) 
data =  {k.lower(): v for k, v in data.items()} #convert all keys to lowercase to avoid misspelling. 

#input
WordDefinition = input("Enter a word: ")
WordDefinition = WordDefinition.lower() #conver the input to lowercase letters. 


#function to get an input and return the definition 
def translator(word):
    # check if word is correct and inside the database
    if word in data:
        return(data[word])
    
    # checking if there is a similar word in database 
    elif len(get_close_matches(word,data.keys())) > 0:
        check =  input("Did you mean %s instead? [Y] or [N]: " %get_close_matches(word,data.keys())[0])
        if check.lower() == "y":
            return (data[get_close_matches(word,data.keys())[0]]) # return the definion of the correct word. 
        elif check.lower() == "n":
            return ("Word does not exist.")
        else:
            return ("Incorrect entry.")
        
    else:
        print("The word you have entered '%s' is not in the databse or has no definition" %word)


#Printing the returned definition 
output = translator(WordDefinition)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)




