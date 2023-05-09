def solve():
    anagram = {}
    n = int(input())
    for i in range(n):
        s = input()
        s = ''.join(sorted(s))
        if s in anagram:
            anagram[s] += 1
        else:
            anagram[s] = 1
    ans = 0
    for i in anagram.values():
        ans += i*(i-1)//2
    print(ans)
