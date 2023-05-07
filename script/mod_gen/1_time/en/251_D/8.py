def main():
    W = int(input())
    if W <= 3:
        print(1)
        print(W)
        return
    ans = []
    for i in range(1, W):
        if i + i + 1 + 1 > W:
            break
        ans.append(i)
        ans.append(i)
        ans.append(i + 1)
        ans.append(i + 1)
        W -= i + i + 1 + 1
    if W == 1:
        ans.append(1)
    elif W == 2:
        ans.append(1)
        ans.append(2)
    elif W == 3:
        ans.append(1)
        ans.append(2)
        ans.append(2)
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()