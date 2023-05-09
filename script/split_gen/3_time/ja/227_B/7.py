def main():
    N = int(input())
    S = list(map(int, input().split()))
    a = 0
    b = 0
    count = 0
    for i in range(N):
        for a in range(1, 1000):
            for b in range(1, 1000):
                if 4*a*b + 3*a + 3*b == S[i]:
                    break
            else:
                continue
            break
        else:
            count += 1
    print(count)
