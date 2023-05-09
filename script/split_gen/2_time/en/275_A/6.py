def main():
    #input
    N = int(input())
    H = list(map(int, input().split()))
    #compute
    ans = H.index(max(H)) + 1
    #output
    print(ans)
