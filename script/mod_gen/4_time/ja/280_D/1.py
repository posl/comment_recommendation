def main():
    k = int(input())
    ans = 1
    for i in range(1,k+1):
        ans = ans * i
        if ans % k == 0:
            print(i)
            break

if __name__ == '__main__':
    main()