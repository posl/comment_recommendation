def main():
    A,B,T = map(int,input().split())
    t = 1
    count = 0
    while t <= T + 0.5:
        if t % A == 0:
            count += B
        t += 1
    print(count)

if __name__ == '__main__':
    main()