Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    c = list(map(int, input(

=======
Suggestion 2

def solve():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    d = {}
    for i in range(k):
        d[c[i]] = d.get(c[i], 0) + 1
    ans = len(d)

    for i in range(n - k):
        d[c[i]] -= 1
        if d[c[i]] == 0:
            del d[c[i]]
        d[c[i + k]] = d.get(c[i + k], 0) + 1
        ans = max(ans, len(d))

    print(ans)

=======
Suggestion 3

def solve():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        d[c[i]] = 1
    ans = len(d)
    for i in range(k, n):
        d[c[i]] = 1
        if d[c[i-k]] == 1:
            del d[c[i-k]]
        ans = max(ans, len(d))
    return ans

print(solve())

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    c = list(map(int,input().split()))
    ans = 0
    d = {}
    for i in range(K):
        if c[i] not in d:
            d[c[i]] = 0
        d[c[i]] += 1
        ans = max(ans,len(d))
    for i in range(K,N):
        d[c[i-K]] -= 1
        if d[c[i-K]] == 0:
            del d[c[i-K]]
        if c[i] not in d:
            d[c[i]] = 0
        d[c[i]] += 1
        ans = max(ans,len(d))
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    colors = {}
    for i in range(n):
        if i >= k:
            colors[c[i-k]] -= 1
            if colors[c[i-k]] == 0:
                del colors[c[i-k]]
        if c[i] not in colors:
            colors[c[i]] = 1
        else:
            colors[c[i]] += 1
        ans = max(ans, len(colors))
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    result = 0
    color = {}
    for i in range(K):
        if C[i] not in color:
            color[C[i]] = 0
        color[C[i]] += 1
    result = len(color)
    for i in range(K, N):
        if C[i - K] in color:
            color[C[i - K]] -= 1
            if color[C[i - K]] == 0:
                del color[C[i - K]]
        if C[i] not in color:
            color[C[i]] = 0
        color[C[i]] += 1
        result = max(result, len(color))
    print(result)

=======
Suggestion 7

def get_max_colors(N, K, c):
    max_colors = 0
    for i in range(N-K+1):
        max_colors = max(max_colors, len(set(c[i:i+K])))
    return max_colors

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    from collections import Counter
    counter = Counter(c[:k])
    max_count = len(counter)
    for i in range(k, n):
        counter[c[i]] += 1
        counter[c[i-k]] -= 1
        if counter[c[i-k]] == 0:
            del counter[c[i-k]]
        max_count = max(max_count, len(counter))

    print(max_count)

=======
Suggestion 9

def main():
    num_candies, num_consecutive = map(int, input().split())
    candies = list(map(int, input().split()))
    max_colors = 0
    for i in range(num_candies-num_consecutive+1):
        max_colors = max(max_colors, len(set(candies[i:i+num_consecutive])))
    print(max_colors)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    # print(n, k)
    # print(c)

    candies = c[:k]
    # print(candies)
    colors = set(candies)
    # print(colors)
    max_colors = len(colors)
    # print(max_colors)

    for i in range(k, n):
        candies.pop(0)
        candies.append(c[i])
        colors = set(candies)
        # print(colors)
        max_colors = max(max_colors, len(colors))
        # print(max_colors)

    print(max_colors)
