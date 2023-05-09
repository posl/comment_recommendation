def main():
    N = int(input())
    P = [int(input()) for i in range(N)]
    P.sort(reverse = True)
    for i in range(N):
        if i == 0:
            total = P[i] / 2
        else:
            total += P[i]
    print(int(total))
