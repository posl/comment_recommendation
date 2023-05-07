def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    ma = max(a)
    ma2 = max(a[:-1])
    for i in range(n):
        if a[i] == ma:
            print(ma2)
        else:
            print(ma)
