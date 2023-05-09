def main():
    n, k = map(int, input().split())
    #print(n, k)
    total = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            total += i*100 + j
    print(total)
