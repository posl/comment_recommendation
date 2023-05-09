def main():
    N = int(input())
    ans = []
    for i in range(2**15):
        if N & i == i:
            ans.append(i)
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()