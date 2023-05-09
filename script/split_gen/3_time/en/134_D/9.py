def main():
    N = int(input())
    a = list(map(int, input().split()))
    #print(N)
    #print(a)
    b = []
    for i in range(N):
        if a[i] == 1:
            b.append(i+1)
    print(len(b))
    for i in range(len(b)):
        print(b[i])
