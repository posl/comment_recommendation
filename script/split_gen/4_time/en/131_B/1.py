def main():
    N, L = map(int, input().split())
    if L > 0:
        print(int(N*(2*L+N-1)/2 - L))
    elif L+N-1 < 0:
        print(int(N*(2*L+N-1)/2 - L))
    else:
        print(int(N*(2*L+N-1)/2))
