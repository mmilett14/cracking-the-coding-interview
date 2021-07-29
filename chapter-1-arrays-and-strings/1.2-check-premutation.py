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
