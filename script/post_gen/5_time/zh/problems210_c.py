Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    #print(n,k,c)
    max = 0
    for i in range(n-k+1):
        #print(c[i:i+k])
        if len(set(c[i:i+k])) > max:
            max = len(set(c[i:i+k]))
    print(max)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    dic = {}
    for i in c[:k]:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    ans = len(dic)
    for i in range(k, n):
        dic[c[i]] = dic.get(c[i], 0) + 1
        dic[c[i-k]] -= 1
        if dic[c[i-k]] == 0:
            del dic[c[i-k]]
        ans = max(ans, len(dic))
    print(ans)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    #print(n,k,c)
    ans = 0
    for i in range(n-k+1):
        ans = max(ans,len(set(c[i:i+k])))
    print(ans)

=======
Suggestion 4

def problem210_c():
    #输入
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    #解法
    ans = 0
    dic = {}
    for i in range(n):
        dic[c[i]] = dic.get(c[i], 0) + 1
        if i >= k:
            dic[c[i - k]] -= 1
            if dic[c[i - k]] == 0:
                del dic[c[i - k]]
        ans = max(ans, len(dic))

    #输出
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    #print(n,k,c)
    ans = 0
    s = set()
    for i in range(k):
        s.add(c[i])
    ans = len(s)
    for i in range(k,n):
        s.add(c[i])
        s.remove(c[i-k])
        ans = max(ans,len(s))
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d = {}
    for i in range(k):
        if c[i] not in d:
            d[c[i]] = 0
        d[c[i]] += 1
    ans = len(d)
    for i in range(k, n):
        d[c[i]] = 1
        d[c[i-k]] -= 1
        if d[c[i-k]] == 0:
            del d[c[i-k]]
        ans = max(ans, len(d))
    print(ans)

=======
Suggestion 7

def main():
    # 读入数据
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    # 预处理
    colors = [0] * (10**9 + 1)
    for i in range(k):
        colors[c[i]] += 1

    # 双指针
    ans = 0
    for i in range(10**9 + 1):
        if colors[i] > 0:
            ans += 1

    for i in range(k, n):
        colors[c[i - k]] -= 1
        if colors[c[i - k]] == 0:
            ans -= 1
        colors[c[i]] += 1
        if colors[c[i]] == 1:
            ans += 1

    # 结果
    print(ans)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    #n,k = 7,3
    #c = [1,2,1,2,3,3,1]
    #n,k = 5,5
    #c = [4,4,4,4,4]
    #n,k = 10,6
    #c = [304621362,506696497,304621362,506696497,834022578,304621362,414720753,304621362,304621362,414720753]
    #print(n,k,c)
    ans = 0
    for i in range(n-k+1):
        tmp = len(set(c[i:i+k]))
        if tmp > ans:
            ans = tmp
    print(ans)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    #print(n, k, candies)
    candy_set = set()
    for i in range(n-k+1):
        candy_set.add(len(set(candies[i:i+k])))
    print(max(candy_set))

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    # 1 <= k <= n <= 3 * 10 ** 5
    # 1 <= c_i <= 10 ** 9
    # n, k = 7, 3
    # c = [1, 2, 1, 2, 3, 3, 1]

    # n, k = 5, 5
    # c = [4, 4, 4, 4, 4]

    # n, k = 10, 6
    # c = [304621362, 506696497, 304621362, 506696497, 834022578, 304621362, 414720753, 304621362, 304621362, 414720753]

    # n, k = 3, 2
    # c = [1, 1, 1]

    # n, k = 3, 2
    # c = [1, 2, 2]

    # n, k = 3, 2
    # c = [1, 2, 1]

    # n, k = 3, 2
    # c = [1, 2, 3]

    # n, k = 3, 2
    # c = [1, 1, 2]

    # n, k = 3, 2
    # c = [1, 1, 3]

    # n, k = 3, 2
    # c = [1, 2, 3]

    # n, k = 3, 2
    # c = [1, 2, 1]

    # n, k = 3, 2
    # c = [1, 2, 3]

    # n, k = 3, 2
    # c = [1, 1, 2]

    # n, k = 3, 2
    # c = [1, 1, 3]

    # n, k = 3, 2
    # c = [1, 2, 3]

    # n, k = 3,
