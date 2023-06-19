def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            print("NO")
            return
    print("YES")
    return
main()
