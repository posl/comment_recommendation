def main():
    n = int(input())
    ans = 'No'
    names = []
    for i in range(n):
        names.append(input().split(' '))
    for i in range(n):
        for j in range(n):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    ans = 'Yes'
                    break
    print(ans)

if __name__ == '__main__':
    main()