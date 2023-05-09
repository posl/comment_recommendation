def main():
    P,Q,R = map(int,input().split())
    print(min(P+Q,Q+R,R+P))
main()

if __name__ == '__main__':
    main()