def search(lst, x, k):
    #print("lst",lst)
    #print("x",x)
    #print("k",k)
    if x not in lst:
        return -1
    else:
        if k > lst.count(x):
            return -1
        else:
            return lst.index(x) + 1
N, Q = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(Q):
    x, k = map(int, input().split())
    print(search(A, x, k))

if __name__ == '__main__':
    search()