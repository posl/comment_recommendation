def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    print(T[N-1]+T[N-2])
