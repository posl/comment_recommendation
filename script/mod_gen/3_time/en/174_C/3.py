def main():
    k = int(input())
    r = 7
    for i in range(k):
        if r % k == 0:
            print(i+1)
            return
        r = (r*10+7) % k
    print(-1)

if __name__ == '__main__':
    main()