def main():
    n = int(input())
    names = [input().split() for _ in range(n)]
    names.sort()
    for i in range(1, n):
        if names[i][0] == names[i-1][0] and names[i][1] == names[i-1][1]:
            print('Yes')
            return
    print('No')
