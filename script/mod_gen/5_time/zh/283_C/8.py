def main():
    S = int(input())
    print(S)
    print(type(S))
    ans = 0
    while S > 0:
        #print(S)
        if S % 100 == 0:
            S /= 100
        else:
            S -= 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()