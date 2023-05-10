def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #print(n, k)
    #print(a)
    #print(b)
    #print(max(a))
    #print(max(b))
    if max(a) > max(b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()