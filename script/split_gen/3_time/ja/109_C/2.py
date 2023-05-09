def main():
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(X)
    x_list.sort()
    D_list = []
    for i in range(N):
        D_list.append(x_list[i+1] - x_list[i])
    D = D_list[0]
    for i in range(1, N):
        D = gcd(D, D_list[i])
    print(D)
