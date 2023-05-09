def main():
    S = input()
    ans = 0
    for i in S:
        if i == "+":
            ans += 1
        else:
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()