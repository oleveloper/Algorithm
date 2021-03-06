# 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    
    for v in arr:
        div = 0
        if v % divisor == 0:
            answer.append(v)
    
    answer = sorted(list(set(answer)))
    if len(answer) == 0:
        answer.append(-1)
    
    return answer
