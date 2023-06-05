def main():
    n = int(input())
    interval = []
    for i in range(n):
        interval.append([int(i) for i in input().split()])
    interval.sort(key=lambda x:x[0])
    stack = [interval[0]]
    for i in range(1,n):
        if stack[-1][1] >= interval[i][0]:
            stack[-1][1] = max(stack[-1][1],interval[i][1])
        else:
            stack.append(interval[i])
    for s in stack:
        print(s[0],s[1])

if __name__ == '__main__':
    main()