import language_check

tool = language_check.LanguageTool('en-US')
compare_dict = {}


def grammar_check(str,i):
    text = str[i]
    matches = tool.check(text)
    no_errors = len(matches)
    compare_dict[no_errors] = str[i]
    
        
        
                                
    
   




        
        
       
        

def sort_answers():
    keys_sorted =  sorted(compare_dict.items(), key=lambda x: x[0])
    final_answer = (keys_sorted)
    return final_answer
    #here first key being most grammatical correct
   



def print_ans():
    sorted_2D_list = sort_answers()
    #print the string containing minimum errors

    #if question is too short ignore it and continue
   
    for i in range(len(sorted_2D_list)):
        currentString = sorted_2D_list[i][1]
        no_of_words = len(currentString.split())
        if(no_of_words <=5):
            continue
        return currentString
    return "not valid string input"  
        
        
    



