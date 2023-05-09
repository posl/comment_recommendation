def main():
    from collections import deque
    K = int(input())
    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for _ in range(K):
        n = q.popleft()
        q.append(n * 10 + n % 10 - 1)
        q.append(n * 10 + n % 10)
        q.append(n * 10 + n % 10 + 1)
    print(n)
