def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = [0] * n
    for i in a:
        m[i-1] += 1
    for i in m:
        print(i)
