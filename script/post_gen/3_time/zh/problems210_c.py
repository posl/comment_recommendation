Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    candy = {}
    for i in range(k):
        if c[i] not in candy:
            candy[c[i]] = 1
        else:
            candy[c[i]] += 1

    ans = len(candy)
    for i in range(k, n):
        if c[i] not in candy:
            candy[c[i]] = 1
        else:
            candy[c[i]] += 1
        candy[c[i - k]] -= 1
        if candy[c[i - k]] == 0:
            del candy[c[i - k]]
        ans = max(ans, len(candy))

    print(ans)

main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    c_set = set()
    for i in range(N-K+1):
        c_set.add(len(set(c[i:i+K])))
    print(max(c_set))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    candy_set = set()
    max_candy = 0
    for i in range(n-k+1):
        for j in range(k):
            candy_set.add(candies[i+j])
        if len(candy_set) > max_candy:
            max_candy = len(candy_set)
        candy_set.clear()
    print(max_candy)

=======
Suggestion 4

def max_color_num(a, k):
    """
    :param a: list
    :param k: int
    :return: int
    """
    if len(a) <= k:
        return len(set(a))
    else:
        max_color = 0
        for i in range(len(a) - k + 1):
            max_color = max(max_color, len(set(a[i:i+k])))
        return max_color

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    s = set()
    for i in range(k):
        s.add(c[i])
    result = len(s)
    for i in range(k, n):
        s.add(c[i])
        s.remove(c[i-k])
        result = max(result, len(s))
    print(result)

=======
Suggestion 6

def solution(N, K, c):
    #print(N, K, c)
    count = 0
    max_count = 0
    for i in range(N):
        if i < K:
            if c[i] not in c[0:i]:
                count += 1
        else:
            if c[i] not in c[i-K:i]:
                count += 1
        if max_count < count:
            max_count = count
        #print("count:", count)
    return max_count

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        d[c[i]] = 1
    ans = len(d)
    for i in range(n-k):
        d[c[i]] -= 1
        if d[c[i]] == 0:
            del d[c[i]]
        if c[i+k] in d:
            d[c[i+k]] += 1
        else:
            d[c[i+k]] = 1
        ans = max(ans, len(d))
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    colors = {}
    for i in range(k):
        if c[i] not in colors:
            colors[c[i]] = 1
        else:
            colors[c[i]] += 1
    max_colors = len(colors)
    for i in range(k, n):
        if c[i] not in colors:
            colors[c[i]] = 1
        else:
            colors[c[i]] += 1
        if colors[c[i-k]] == 1:
            del colors[c[i-k]]
        else:
            colors[c[i-k]] -= 1
        if len(colors) > max_colors:
            max_colors = len(colors)
    print(max_colors)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    #print(c)
    #print(n, k)
    #print(c[0])
    #print(c[n-1])
    #print(c[n-1] - c[0])
    if n == k:
        print(1)
    else:
        print(n - k + 1)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    # print(N, K, C)
    # N, K = 7, 3
    # C = [1, 2, 1, 2, 3, 3, 1]
    # N, K = 5, 5
    # C = [4, 4, 4, 4, 4]
    # N, K = 10, 6
    # C = [304621362, 506696497, 304621362, 506696497, 834022578, 304621362, 414720753, 304621362, 304621362, 414720753]
    # N, K = 300000, 300000
    # C = [i for i in range(1, 300001)]
    # N, K = 300000, 1
    # C = [i for i in range(1, 300001)]
    # N, K = 300000, 300000
    # C = [i for i in range(1, 300001)]
    # N, K = 1, 1
    # C = [1]
    # N, K = 300000, 2
    # C = [i for i in range(1, 300001)]
    # N, K = 300000, 3
    # C = [i for i in range(1, 300001)]
    # N, K = 300000, 4
    # C = [i for i in range(1, 300001)]
    # N, K = 300000, 5
    # C = [i for i in range(1, 300001)]
    # N, K = 300000, 6
    # C = [i for i in range(1, 300001)]
    # N, K = 300000, 7
    # C = [i for i in range(1, 300001)]
    # N, K = 300000, 8
    # C = [i for i in range(1, 300001)]
    # N, K = 300000,
