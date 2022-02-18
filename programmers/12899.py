# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    if n < 4:
        return '124'[n - 1]
    else:
        q, r = divmod(n - 1, 3)
        return solution(q) + '124'[r]
