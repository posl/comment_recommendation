def search(x):
    if x == 1:
        return 1
    elif x == 2:
        return 0
    else:
        if x in dict:
            return dict[x]
        else:
            dict[x] = search(x-1) + search(x-2)
            return dict[x]
N,M = map(int,input().split())
dict = {}
for i in range(M):
    A,B = map(int,input().split())
    if A in dict:
        dict[A] += 1
    else:
        dict[A] = 1
    if B in dict:
        dict[B] += 1
    else:
        dict[B] = 1
print(dict)
print(search(N))
