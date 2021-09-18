# Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(string0, string1):
    
    letter_match = 0
    
    if len(string0) != len(string1):
        print("strings are different lengths - they are not permutations!")
    
    else:
        for i in range(0,len(string0)):
            
            for j in range(0,len(string1)):
            
                if string0[i] == string1[j]:
                    letter_match += 1
                    break
                
        if letter_match == len(string0):
            print("congratulations, it's a permutation!")
        
        else:
            print("they are not permutations!")

def check_permutation_better(str0, str1):

    str_dict0 = {}
    str_dict1 = {}
    
    for i in range(0, len(str0)):

        if str0[i] not in str_dict0:
            str_dict0[str0[i]] = 1

        elif str0[i] in str_dict0:
            str_dict0[str0[i]] += 1 
    
    for i in range(0, len(str1)):

        if str1[i] not in str_dict1:
            str_dict1[str1[i]] = 1

        elif str1[i] in str_dict1:
            str_dict1[str1[i]] += 1 
    
    if str_dict0 == str_dict1:
        print('they match!')
    
    else:
        print('they dont match!')
