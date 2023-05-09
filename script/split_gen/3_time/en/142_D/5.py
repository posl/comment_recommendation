def main():
    A, B = map(int, input().split())
    print(len(set(gcd(A, B))))
