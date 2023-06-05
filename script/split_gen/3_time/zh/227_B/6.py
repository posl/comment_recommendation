def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(0,N):
        a = 1
        b = 1
        while a*b < S[i]:
            if a == b:
                b += 1
            else:
                a += 1
        if a*b != S[i]:
            count += 1
    print(count)
