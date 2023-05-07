def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    total = sum(A)
    #print(total)
    if T % total == 0:
        print(N, 0)
        return
    else:
        T = T % total
        #print(T)
        for i, a in enumerate(A):
            if T <= a:
                print(i + 1, T)
                return
            else:
                T -= a
        return
