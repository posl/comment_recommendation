def solve():
    from collections import deque
    K = int(input())
    Q = deque([1,2,3,4,5,6,7,8,9])
    for i in range(K):
        x = Q.popleft()
        if x%10 != 0:
            Q.append(10*x + x%10 - 1)
        Q.append(10*x + x%10)
        if x%10 != 9:
            Q.append(10*x + x%10 + 1)
    print(x)
solve()
