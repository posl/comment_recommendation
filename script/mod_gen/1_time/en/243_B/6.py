def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    same = 0
    diff = 0
    for i in range(n):
        if a[i] == b[i]:
            same += 1
    for i in range(n):
        for j in range(n):
            if i != j and a[i] == b[j]:
                diff += 1
    print(same)
    print(diff)

if __name__ == '__main__':
    main()