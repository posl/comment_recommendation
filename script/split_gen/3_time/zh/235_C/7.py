def search(x,k):
    index = 0
    for i in range(k):
        index = A.index(x,index)
        if index == -1:
            return -1
        index += 1
    return index
N,Q = input().split()
N = int(N)
Q = int(Q)
A = input().split()
A = [int(i) for i in A]
for i in range(Q):
    x,k = input().split()
    x = int(x)
    k = int(k)
    print(search(x,k))
