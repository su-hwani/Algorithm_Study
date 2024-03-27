def solution(brown, yellow):
    if yellow == 1:
        return [3,3]
    answer = []
    for i in range(1, yellow//2+1):
        yellow_block = [i, yellow//i]
        if yellow % i == 0:
            brown_block_count = (yellow_block[0]+2) * 2 + yellow_block[1] * 2
            if brown == brown_block_count:
                answer = [yellow_block[1]+2, yellow_block[0]+2]
                break 
    
    
    
    return answer
 