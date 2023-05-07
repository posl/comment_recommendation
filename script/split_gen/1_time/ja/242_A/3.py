def main():
    A, B, C, X = map(int, input().split())
    ans = 0
    for i in range(A):
        ans += 1
    for i in range(A, B):
        ans += C/(B-A)
    for i in range(B, X):
        ans += 0
    print(ans)
