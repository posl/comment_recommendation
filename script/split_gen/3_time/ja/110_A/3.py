def main():
    A, B, C = map(int, input().split())
    print(A+B+C+max(A*10+B+C, B*10+A+C, C*10+A+B))
