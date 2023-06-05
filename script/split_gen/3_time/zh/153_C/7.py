def main():
    #N, K = map(int, input().split())
    #H = list(map(int, input().split()))
    N, K = 3, 1
    H = [4, 1, 5]
    #N, K = 8, 9
    #H = [7, 9, 3, 2, 3, 8, 4, 6]
    #N, K = 3, 0
    #H = [1000000000, 1000000000, 1000000000]
    H.sort()
    H.reverse()
    #print(H)
    print(sum(H[K:]))
