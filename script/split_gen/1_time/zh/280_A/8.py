def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    count = 0
    for i in range(H):
        count += S[i].count('#')
    print(count)
