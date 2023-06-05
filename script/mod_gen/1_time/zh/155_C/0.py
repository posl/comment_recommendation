def solve():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
    
    max_v = max(d.values())
    for k, v in d.items():
        if v == max_v:
            print(k)

if __name__ == '__main__':
    solve()