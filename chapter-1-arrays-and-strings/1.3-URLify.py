# Write a method to replace all spaces in a string with '%20'.

def urlify(string):
    
    space_list = []
    
    for i in range(0, len(string0)):
        if string[i] == ' ':
            space_list.append(i)
            
    string_start = 0
    string_end = len(string)-1
    
    string_final = ''
    
    print(space_list)
    
    for i in range(0, len(space_list)):
        
        if i == 0:
            string_part = string[0:space_list[i]]
            
            string_final = string_final + string_part + '%20' + string[space_list[i]-1:space_list[i+1]]
        
        elif i == len(space_list)-1:
            string_part = string[space_list[i]-1:len(string)]
            
            string_final = string_final + '%20' + string_part
            
        else:
            string_part = string[space_list[i]-1:space_list[i+1]]
            
            string_final = string_final + '%20' + string_part
    
    print(string_final)
