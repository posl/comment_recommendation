def main():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            ans.append(i)
            if N//i != i:
                ans.append(N//i)
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()