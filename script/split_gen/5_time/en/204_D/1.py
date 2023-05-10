def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    if N == 1:
        print(T[0])
    elif N == 2:
        print(max(T[0], T[1]))
    else:
        print(max(T[0], T[1]) + min(T[0], T[1]) + sum(T[2:]))
