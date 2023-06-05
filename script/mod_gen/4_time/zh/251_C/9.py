def problems251_c():
    n = int(input())
    best = 0
    best_score = 0
    best_time = 10**10
    for i in range(n):
        s,t = input().split()
        t = int(t)
        if t > best_score:
            best_score = t
            best = i
            best_time = 10**10
        elif t == best_score:
            if s == s:
                best = i
                best_time = 10**10
            else:
                best_time = min(best_time,i)
    print(best+1)

if __name__ == '__main__':
    problems251_c()