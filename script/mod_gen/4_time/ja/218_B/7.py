def main():
    p = list(map(int, input().split()))
    ans = [chr(p[i]+96) for i in range(26)]
    print("".join(ans))

if __name__ == '__main__':
    main()