# 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a

    for v in range(a, b + 1):
        answer += v
    
    return answer
