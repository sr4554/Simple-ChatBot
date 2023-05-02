import re
import longresponses as long

def message_prob(user_message,rec_words,single_res=False,req_words=[]):
    message_certainity=0
    has_req_words=True

    for word in user_message:
        if word in rec_words:
            message_certainity+=1
    
    percentage=float(message_certainity)/float(len(rec_words))
    

    for word in rec_words:
        if word not in user_message:
            has_req_words=False
            break

    if has_req_words or single_res:
        return int(percentage*100)
    else:
        return 0
    
def check_all_messages(message):
    high_prob_list={}
        
    def response(bot_response,list_of_words,single_res=False, req_words=[]):
        nonlocal high_prob_list
        high_prob_list[bot_response] =message_prob(message,list_of_words, single_res ,req_words)

    #Responses -------------------------------------------------------------------------------------------------
    response('Hello!',['hello','hi','sup','hey','heyo','yes'],single_res=True)
    response('I am doing fine and you?',['how','are','you','doing'],req_words=['how'])
    response('Have a great day!',['see','you','later'],req_words=['see','later'])
    response('That is great',['I','am','good'],req_words=['i','good'])
    response('Thank You!',['i','like','coding','with','you'],req_words=['coding'])
    response(long.R_JOKE,['tell','me','a','joke'],req_words=['tell','joke'])
    response(long.R_WEATHER,['how','is','the','weather','today'],req_words=['waether','today'])
    response('Anything else?',['no','I','am','done'],req_words=['no','done'])

    best_match=max(high_prob_list,key=high_prob_list.get)
    #print(high_prob_list)

    return long.unknown() if high_prob_list[best_match] < 1 else best_match



def get_response(user_input):
    split_message=re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response=check_all_messages(split_message)
    return response

print("Do you want to chat?")
while True:
    print('Bot: ' + get_response(input('You: ')))