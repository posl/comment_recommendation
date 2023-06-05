def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B-C, A-B+C, A-B-C, A+B*C, A+B*C, A-B*C, A-B*C))
