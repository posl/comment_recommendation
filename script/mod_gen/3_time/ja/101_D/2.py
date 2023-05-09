def main():
    K = int(input())
    ans = []
    for i in range(1, 10):
        ans.append(i)
    for i in range(10, 10**15):
        if i % sum(map(int, str(i))) == 0:
            ans.append(i)
        if len(ans) > K:
            break
    for i in range(K):
        print(ans[i])

if __name__ == '__main__':
    main()