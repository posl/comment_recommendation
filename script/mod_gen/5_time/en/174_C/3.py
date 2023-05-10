def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        s = 7
        for i in range(k):
            if s % k == 0:
                print(i+1)
                break
            else:
                s = (s * 10 + 7) % k

if __name__ == '__main__':
    main()