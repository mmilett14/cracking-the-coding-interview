def palindrome_permutation(string):
    
    string = string.lower().replace(" " , "")
    
    letter_counter = {}
    
    odd_counter = 0
    
    for char in string:
        
        if char not in letter_counter:
            letter_counter[char] = 1
        
        else:
            letter_counter[char] += 1
            
            
        if letter_counter[char] % 2 == 1:
            odd_counter += 1
    
        else:
            odd_counter -=1 
    
    if odd_counter > 1:
        return False
    
    else:
        return True
