def main():
    n = int(input())
    for i in range(n):
        a = list(map(int, input().split()))
        if a[0] == 1:
            A.append(a[1])
        elif a[0] == 2:
            print(max(sorted(A)[:a[2]]))
        else:
            print(min(sorted(A)[::-1][:a[2]]))
A = []
main()
