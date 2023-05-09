def main():
    N = int(input())
    S = input()
    ans = [0]
    for i in range(1, N):
        if S[i-1] == 'R':
            ans.append(i+1)
        else:
            ans.insert(0, i+1)
    print(*ans)

if __name__ == '__main__':
    main()