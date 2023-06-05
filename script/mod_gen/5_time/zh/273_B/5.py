def main():
    x,k = input().split()
    x = int(x)
    k = int(k)
    for i in range(k):
        if x%10 == 0:
            x = x//10
        else:
            x = x+1
    print(x)

if __name__ == '__main__':
    main()