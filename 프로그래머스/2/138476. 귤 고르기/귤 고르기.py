def solution(k, tangerine):
    diction = {}
    for i in tangerine:
        if i not in diction: 
            diction[i] = 1
        else:
            diction[i] += 1

    
    answer = sorted(diction.items(), key=lambda item: item[1], reverse=True)
    answer_count = 0

    
    for i in answer:
        k -= i[1]
        answer_count += 1
        if k <= 0: 
            return answer_count 


