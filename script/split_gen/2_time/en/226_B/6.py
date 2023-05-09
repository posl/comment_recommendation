def main():
    N = int(input())
    count = 0
    for i in range(N):
        L = input().split()
        L = [int(x) for x in L]
        L = L[1:]
        if len(set(L)) == len(L):
            count += 1
    print(count)
