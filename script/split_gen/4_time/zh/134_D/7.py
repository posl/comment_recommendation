def main():
    N = int(input())
    a = list(map(int,input().split()))
    b = [0]*N
    for i in range(N):
        if a[i] == 1:
            if i+1 < N:
                b[i+1] = 1
            else:
                b[0] = 1
    print(sum(b))
    for i in range(len(b)):
        if b[i] == 1:
            print(i+1)
