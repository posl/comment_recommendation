def main():
    # ここに処理を書きます
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B*C, A*B+C, A*B*C, (A+B)*C, A*(B+C)))
