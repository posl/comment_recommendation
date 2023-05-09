def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = set(A)
    b = set(B)
    c = a&b
    d = a^b
    print(len(c))
    print(len(d))
