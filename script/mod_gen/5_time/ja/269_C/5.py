def main():
    n = int(input())
    ans = []
    for i in range(2**15):
        if n & i == i:
            ans.append(i)
    print("\n".join(map(str, ans)))

if __name__ == '__main__':
    main()