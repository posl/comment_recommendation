def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        a = 0
        b = 0
        for j in range(1,1000):
            if (S[i] - 3*j) % (4*j) == 0:
                a = j
                b = (S[i] - 3*j) // (4*j)
                break
        if 4*a*b + 3*a + 3*b != S[i]:
            count += 1
    print(count)
