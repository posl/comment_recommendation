def main():
    n = int(input())
    a = [0] * (n-1)
    b = [0] * (n-1)
    for i in range(n-1):
        a[i], b[i] = map(int, input().split())
    #print(a)
    #print(b)
    #print(n)
    for i in range(n-1):
        if a[i] == 1 or b[i] == 1:
            return print("Yes")
    return print("No")

if __name__ == '__main__':
    main()