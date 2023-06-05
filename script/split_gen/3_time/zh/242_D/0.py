def main():
    s = input()
    q = int(input())
    for i in range(q):
        t, k = map(int, input().split())
        while t > 0:
            k = (k + 2) // 3
            t -= 1
        print(s[k - 1])
