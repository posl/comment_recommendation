def main():
    n = int(input())
    num = [0] * n
    for a in map(int, input().split()):
        num[a - 1] ^= 1
    print(num.index(1) + 1)
