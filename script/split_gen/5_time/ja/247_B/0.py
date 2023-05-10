def main():
    n = int(input())
    names = [input().split() for i in range(n)]
    names = [name[0] + ' ' + name[1] for name in names]
    for i in range(n):
        for j in range(n):
            if i != j and names[i] == names[j]:
                print('Yes')
                return
    print('No')
