def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(list(input().split()))
    for i in range(N):
        if name[i][0] in name[i][1] or name[i][1] in name[i][0]:
            continue
        else:
            for j in range(N):
                if i == j:
                    continue
                if name[i][0] in name[j] or name[i][1] in name[j]:
                    continue
                else:
                    print('No')
                    return
    print('Yes')
