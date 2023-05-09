def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    modA = [a % mod for a in A]
    #print(modA)
    modAtoIndex = [[] for _ in range(mod)]
    for i in range(N):
        modAtoIndex[modA[i]].append(i)
    #print(modAtoIndex)
    for i in range(mod):
        if len(modAtoIndex[i]) >= 2:
            print("Yes")
            print(1, modAtoIndex[i][0] + 1)
            print(1, modAtoIndex[i][1] + 1)
            return
    for i in range(mod):
        for j in range(i + 1, mod):
            if len(modAtoIndex[i]) >= 1 and len(modAtoIndex[j]) >= 1:
                print("Yes")
                print(2, modAtoIndex[i][0] + 1, modAtoIndex[j][0] + 1)
                print(1, modAtoIndex[i][0] + 1)
                return
    print("No")
    return
