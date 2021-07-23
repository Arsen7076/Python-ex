def check_str(str1):
    if len(str1)<7:
        raise ValueError (f'The number of characters in the input {str1} is not >=7')
    elif len(str1)%2==0 : 
        raise ValueError(f'The number of characters in the input {str1} is not odd')
    elif type(str1)!= str:
        raise ValueError(f'The input {str1} is not of type {str}!')
    else:
        pass
def midle_str(str1):
    check_str(str1) #check the input against the conditions
    beg=(len(str1)//2)-1 #Select the begining index 
    end=(len(str1)//2)+2 #select the end index
    str3= str1[beg:end] #Slice the  string based on the midle character
    return str3
def ex2 (str4,str5):
    mid=(len(str4)//2) #Select the midle index
    endstr=str4[:mid]+str5+str4[mid:] #Plas the two strings 
    return endstr
a=input("Enter a first string ")#input string 
b=input("Enter a second string ") #input second string
print(midle_str(a))
print(midle_str(b))
print(ex2(a,b))