def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(tuple(map(int, input().split())))
    L.sort(key=lambda x: x[0])
    #print(L)
    c = 0
    for i in range(N):
        #print("i", i)
        for j in range(i + 1, N):
            #print("j", j)
            if L[i][0] == L[j][0]:
                if L[i][1:] == L[j][1:]:
                    L[j] = ()
                else:
                    c += 1
            else:
                break
    #print(L)
    print(N - c)
