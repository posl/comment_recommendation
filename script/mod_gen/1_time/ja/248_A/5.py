def main():
    S = input()
    ans = 0
    for i in range(10):
        if str(i) not in S:
            ans = i
    print(ans)

if __name__ == '__main__':
    main()