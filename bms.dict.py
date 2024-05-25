string = 'immunology is an attractive science'

counter = dict ()

for letter in string:    
    
    if letter in counter:    
        counter[letter] += 1
    else:    
        counter[letter] = 1
        print (counter)
        print (letter, counter)
        