def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max2 = sorted(a)[-2]
    for i in range(n):
        if a[i] == a_max:
            print(a_max2)
        else:
            print(a_max)
