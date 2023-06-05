def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    for i in range(K):
        H.pop()
    print(sum(H))
main()
