def main():
    n = int(input())
    a = []
    for i in range(n):
        line = input().split()
        if line[0] == '1':
            a.append(int(line[1]))
        elif line[0] == '2':
            x = int(line[1])
            k = int(line[2])
            tmp = []
            for j in range(len(a)):
                if a[j] <= x:
                    tmp.append(a[j])
            tmp.sort()
            if len(tmp) < k:
                print(-1)
            else:
                print(tmp[-k])
        else:
            x = int(line[1])
            k = int(line[2])
            tmp = []
            for j in range(len(a)):
                if a[j] >= x:
                    tmp.append(a[j])
            tmp.sort()
            if len(tmp) < k:
                print(-1)
            else:
                print(tmp[k-1])
