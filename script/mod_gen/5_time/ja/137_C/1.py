def solve():
    N = int(input())
    words = [input() for _ in range(N)]
    #print(words)
    d = {}
    for word in words:
        #print(word)
        word = ''.join(sorted(word))
        #print(word)
        d[word] = d.get(word, 0) + 1
        #print(d)
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()