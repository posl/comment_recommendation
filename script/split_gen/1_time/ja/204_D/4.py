def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    if N == 1:
        print(T[0])
    else:
        print(T[0]+sum(T[1:N-1])+int(T[N-1]/2))
