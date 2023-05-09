def main():
    A, B = map(int, input().split())
    def S(n):
        return sum(map(int, str(n)))
    print(max(S(A), S(B)))
