def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    #print(len(a))
    #print(len(set(a)))
    if len(a) == len(set(a)):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()