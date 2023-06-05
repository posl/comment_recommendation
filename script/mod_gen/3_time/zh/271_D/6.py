def main():
    N, S = map(int, input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    ans = []
    for i in range(N):
        if AB[i][0] == S:
            ans.append("H")
        elif AB[i][1] == S:
            ans.append("T")
        elif AB[i][0] + AB[i][1] == S:
            ans.append("HT")
        else:
            ans.append("N")
    if "N" in ans:
        print("No")
    else:
        print("Yes")
        print("".join(ans))

if __name__ == '__main__':
    main()