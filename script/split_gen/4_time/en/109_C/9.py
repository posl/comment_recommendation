def main():
    N, X = map(int, input().split())
    x = [int(i) for i in input().split()]
    # x と X の差分を求める
    x = [abs(i - X) for i in x]
    # x と X の最大公約数を求める
    a = x[0]
    for i in range(1, len(x)):
        b = x[i]
        while b:
            a, b = b, a % b
    print(a)
