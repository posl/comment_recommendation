def max_k(n, k, arr):
    from collections import deque
    d = deque()
    for i in range(n):
        while d and arr[d[-1]] <= arr[i]:
            d.pop()
        d.append(i)
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            print(arr[d[0]])

if __name__ == '__main__':
    max_k()