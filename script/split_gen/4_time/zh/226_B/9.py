def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(input().split())
    for i in range(N):
        L[i] = [int(x) for x in L[i]]
    L.sort()
    count = 1
    for i in range(1,N):
        if(L[i] != L[i-1]):
            count += 1
    print(count)
