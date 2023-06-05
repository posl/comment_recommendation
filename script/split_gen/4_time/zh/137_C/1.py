def problem137_c():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if s[i] == s[j]:
                count += 1
    print(count)
