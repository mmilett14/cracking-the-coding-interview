def one_away(str0, str1):
    
    len0 = len(str0)
    len1 = len(str1)
    
    if len0 > len1:
        big, lil = str0, str1
    
    else:
        big, lil = str1, str0
    
    if abs(len0 - len1) > 1:
        return -1
    
    elif abs(len0 - len1) == 0:
        
        diff = 0
        
        for i in range(0, len(big)):
            
            if big[i] != lil[i]:
                diff +=1
        
    elif abs(len0 - len1) == 1:
    
        diff = 0
        j = 0

        for i in range(0, len(big)-1):

            if (j <= len(lil)) & (big[i] == lil[j]):
                j += 1

            else:
                diff += 1

    if diff > 1:
        return -1

    else:
        return 0
