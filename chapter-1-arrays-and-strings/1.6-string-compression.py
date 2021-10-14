def string_compress(string):
    
    letter_counter = 1
    compressed_str = ''
    
    for i in range(len(string)-1):
        
        if (i == len(string)-2) & (string[i] == string[i+1]):
            letter_counter += 1
            compressed_str += string[i] + str(letter_counter)
            
        elif (i == len(string)-2) & (string[i] != string[i+1]):
            letter_counter = 1
            compressed_str += string[i] + str(letter_counter)
        
        elif string[i] == string[i+1]:
            letter_counter += 1
        
        else:
            compressed_str += string[i] + str(letter_counter)
            letter_counter = 1
            
    if len(compressed_str) < len(string):
        return compressed_str
    
    else:
        return string
