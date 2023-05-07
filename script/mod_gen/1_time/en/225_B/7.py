def main():
    N = int(input())
    a = [0]*N
    b = [0]*N
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    if max(a) == max(b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()