def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        if name in names:
            print('Yes')
            break
        else:
            names.append(name)
    else:
        print('No')
