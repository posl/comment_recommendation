def solution(N):
    count = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            count += 1
    return count
N = int(input())
print(solution(N))
