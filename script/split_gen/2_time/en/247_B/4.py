def main():
    n = int(input())
    names = [tuple(input().split()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                print('No')
                return
    print('Yes')
