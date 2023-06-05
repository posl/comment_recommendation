def main():
    q = int(input())
    a = []
    for i in range(q):
        a.append(input().split())
    for i in range(q):
        if int(a[i][0]) == 1:
            print(a[i][1] + a[i][2])
        else:
            print(int(a[i][1]) + int(a[i][1]) + 1)
main()
