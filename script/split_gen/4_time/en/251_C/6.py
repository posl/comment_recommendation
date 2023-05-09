def main():
    #N = int(input())
    #S = [input() for i in range(N)]
    #T = [int(input()) for i in range(N)]
    N = 10
    S = ['bb', 'ba', 'aa', 'bb', 'ba', 'aa', 'aa', 'ab', 'bb', 'ab']
    T = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    d = {}
    for i in range(N):
        if S[i] in d:
            d[S[i]].append((T[i], i))
        else:
            d[S[i]] = [(T[i], i)]
    #print(d)
    for k, v in d.items():
        d[k] = sorted(v, key=lambda x: x[0], reverse=True)
    #print(d)
    ans = sorted(d.items(), key=lambda x: x[1][0][0], reverse=True)[0][1][0][1]
    print(ans + 1)
