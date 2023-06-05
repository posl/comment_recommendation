def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        names.append(name)
    for i in range(n-1):
        for j in range(i+1,n):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print('Yes')
                exit()
    print('No')
