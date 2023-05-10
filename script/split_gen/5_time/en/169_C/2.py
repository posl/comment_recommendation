def main():
    A, B = map(str, input().split())
    A = int(A)
    B = B.replace('.', '')
    B = int(B)
    ans = A * B // 100
    print(ans)
