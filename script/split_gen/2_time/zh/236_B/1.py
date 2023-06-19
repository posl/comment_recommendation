def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != a[1]:
        print(a[0])
    elif a[-1] != a[-2]:
        print(a[-1])
    else:
        for i in range(1, len(a)-1):
            if a[i] != a[i-1] and a[i] != a[i+1]:
                print(a[i])
                break
