# count vovels
# count special charater
# count special word
# count multiple word in text
# remove extra space
# count space
# remove space or tabs
# remove all extra charaters
#

punctuaution_list=[',','.',':',';','?','/','!','*','-','_','(',')','[',']','{','}','|','/','...','\'','\"',"+","=","&","^","~","`","<",">","|"]

def Count_Punctuation(text):
    """Enter you text or payragraph for counting the total punctuation and its return  the total count """
    count=0
    for x in range(len(text)):
        if text[x] in punctuaution_list:
            count=count+1
    return count




def Remove_Punctuation(text):
    """Remove Puntuation from the given value"""
    result=""
    for x in range(len(text)):
        if text[x] not in punctuaution_list:
            result=result+text[x]

            
    return result



def Count_Special_Word(text,word):
    """Count special word in your data e.g count Apple in( I like Apple and you want apple)"""
    new_text=text.split(' ')
    
    count=0
    for x in range(len(new_text)):
        if word.lower() == new_text[x].lower():
            
            count=count+1
    return count        



def Remove_Special_Word(text,word):
    """Remove special word from your data e.g remove all cat from data"""
    new_text=text.split(' ')
    result=""
  
    for x in range(len(new_text)):
        if word.lower() != new_text[x].lower():
            result= result+new_text[x]+" "
          
    return result


def Replace_Specail_Word(text,selected_word,replace_by):
    """Select the special word and replace it with your own word from data"""
    string=" "
    new_text=text.split(' ')
    for x in range(len(new_text)):
        if selected_word.lower() == new_text[x].lower():
            new_text[x]=replace_by
    return string.join(new_text)        

def Count_Vovils(text):
    """Count all vovils from your data"""
    vovils=['a','e','i','o','','A','E','I','O','U']
    # count=0
    for x in range(len(text)):
        count=0
        if text[x] in vovils:
            count=count+1            
    return count

def Count_Allspace(text):

    """Count space tabs and new line and return int value"""
   
    count=0
    for x in range(len(text)):
        if text[x]==' ' or text[x]=='\n' or text[x]=='\t':
            count=count+1
    return count 

# def Count_Tabs(text):
#     """Count only tabs and return int value"""
#     new_text=text.split(' ')
#     count=0
#     for x in range(len(new_text)):
#         if  new_text[x]=='\t':
#             count=count+1
#     return count 


# def Remove_Tabs(text):
#     """Remove only tabs"""
#     new_text=text.split(' ')
#     count=0
#     for x in range(len(new_text)):
#         if  new_text[x]=='\t':
#             count=count+1
#     return count 

def Count_Palindrom(text):
    """Count all palindroms in your given data"""
    new_text=text.split(' ')
    count=0
    for value in new_text:
        if value == value[::-1]:
            count=count+1
    return count 

def List_of_Palindrom(text):
    """This funtion return the list of palindroms"""
    new_text=text.split(' ')
    Palindroms=[]
    for value in new_text:
        if value == value[::-1]:
            Palindroms.append(value)
    return Palindroms 

def Count_Articals(text):
    """Count articals in your given data"""
    Artical_list=["a","an","the"]
    new_text=text.split(' ')
    count=0
    for value in new_text:
        if value.lower() in Artical_list:
            count=count+1
    return count        

def Remove_Articals(text):
    """Remove Artical in given data"""
    Artical_list=["a","an","the"]
    new_text=text.split(' ')
    result=""
    for value in new_text:
        if value.lower() not in Artical_list:
            result=result+value
            
    return result


def Remove_Helping_Verbs(text):
    """Remove all heling verbs in given data"""
    new_text=text.split(' ')
    result=" "
    Helping_Verbs=["is","am","are","was","were","did","do","does","has","have","been","being","be"]
    for value in new_text:
        if value.lower() not in Helping_Verbs:

            result=result+value+" "
    return result        

def Count_Helping_Verbs(text):
    new_text=text.split(' ')
    count=0
    Helping_Verbs=["is","am","are","was","were","did","do","does","has","have","been","being","be"]
    for value in new_text:
        if value.lower() in Helping_Verbs:
            count=count+1
    return count
    
def Remove_Artical_SpecialCharacter_Helpingverbs(text):
    """This funtion return the all special character/puncturation , artical and heling verbs """
    specialcharacter=Remove_Punctuation(text)
    removeartical=Remove_Articals(specialcharacter)
    remove_helpingverb=Remove_Helping_Verbs(removeartical)
    return remove_helpingverb