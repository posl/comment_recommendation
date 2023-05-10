def problems216_b():
    n = int(input())
    names = []
    for i in range(n):
        s,t = input().split()
        names.append((s,t))
    for i in range(n):
        for j in range(i+1,n):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    problems216_b()