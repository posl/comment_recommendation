def main():
    P, Q, R = map(int, input().split())
    print(min(P + Q, P + R, Q + R))

if __name__ == '__main__':
    main()