def main():
    N = int(input())
    H = list(map(int, input().split()))
    #print(N)
    #print(H)
    max = 0
    for i in range(N):
        if max <= H[i]:
            max = H[i]
    print(max)
