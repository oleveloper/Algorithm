# 정수 삼각형
# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
    
    return max(dp[len(triangle) - 1])
