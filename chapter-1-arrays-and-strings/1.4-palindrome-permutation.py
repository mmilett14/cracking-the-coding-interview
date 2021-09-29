def palindrome_permutation(string):
     
    if len(string) % 2 == 0:
        return -1
    
    letter_counter = {}
    
    odd_counter = 0
    
    for i in range(0, len(string)):
        
        if string[i] not in letter_counter:
            letter_counter[string[i]] = 1
            odd_counter += 1
            
        else:
            letter_counter[string[i]] += 1
            odd_counter -= 1
            
    if odd_counter > 1:
        return -1
    
    else:
        return 0
