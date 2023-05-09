def main():
    N, K = map(int, input().split())
    friend = []
    for i in range(N):
        A, B = map(int, input().split())
        friend.append([A, B])
    friend.sort()
    for i in range(N):
        if K < friend[i][0]:
            break
        K += friend[i][1]
    print(K)
