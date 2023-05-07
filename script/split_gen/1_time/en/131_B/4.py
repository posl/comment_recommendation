def main():
    N,L = map(int,input().split())
    if L <= 0 and L+N-1 >= 0:
        print(sum(range(L,L+N)))
    elif L <= 0 and L+N-1 < 0:
        print(sum(range(L,L+N-1)))
    else:
        print(sum(range(L+1,L+N)))
