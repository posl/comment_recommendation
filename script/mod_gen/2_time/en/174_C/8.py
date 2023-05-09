def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
    else:
        mod = 7
        for i in range(10**6):
            if mod % k == 0:
                print(i+1)
                break
            mod = mod * 10 + 7
        else:
            print(-1)

if __name__ == '__main__':
    main()