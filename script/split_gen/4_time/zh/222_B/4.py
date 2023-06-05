def main():
    N,P = input().split()
    N = int(N)
    P = int(P)
    a = input().split()
    count = 0
    for i in range(N):
        if int(a[i]) < P:
            count += 1
    print(count)
