def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    max_height = 0
    for i in range(n):
        if a[i] < max_height:
            print("No")
            return
        if a[i] > max_height:
            max_height = a[i]
            a[i] -= 1
    print("Yes")
