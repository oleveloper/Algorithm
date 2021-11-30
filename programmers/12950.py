# 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        answer.append([x + y for x, y in zip(arr1[i], arr2[i])])
    
    return answer
