def main():
    A, B = map(int, input().split())
    print(max(A+B, A*2-1, B*2-1))
