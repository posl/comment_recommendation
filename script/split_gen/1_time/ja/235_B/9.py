def main():
    N = int(input())
    H = list(map(int, input().split()))
    #print(N)
    #print(H)
    max_height = 0
    for i in range(N):
        if H[i] >= max_height:
            max_height = H[i]
    print(max_height)
