def main():
    n = int(input())
    a = [0] * n
    for i in map(int, input().split()):
        a[i - 1] += 1
    for x in a:
        print(x)
