def problem137_c():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s.sort()
    #print(s)
    count = 0
    i = 0
    while i < N:
        j = i + 1
        while j < N:
            if s[i] == s[j]:
                count += 1
            else:
                break
            j += 1
        i = j
    print(count)
