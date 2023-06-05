def main():
    s = input()
    t = s.replace('?', 'A')
    q = s.count('?')
    ans = 0
    for i in range(q+1):
        for j in range(q+1-i):
            k = q - i - j
            tmp = t
            tmp = tmp.replace('A', 'B', i)
            tmp = tmp.replace('B', 'C', j)
            tmp = tmp.replace('C', 'A', k)
            ans += tmp.count('ABC')
    print(ans % (10**9+7))
