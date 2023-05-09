def main():
    P,Q,R = map(int, input().split())
    print(min(P+Q, Q+R, R+P))
    return

if __name__ == '__main__':
    main()