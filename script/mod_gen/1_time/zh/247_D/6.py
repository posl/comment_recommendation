def main():
    import sys
    from collections import deque
    q = int(input())
    queries = [sys.stdin.readline().strip() for i in range(q)]
    ans = deque()
    num = 0
    for query in queries:
        q = query.split()
        if q[0] == '1':
            num += int(q[2])
            if q[1] == '1':
                ans.appendleft(int(q[2]))
            else:
                ans.append(int(q[2]))
        else:
            temp = 0
            for i in range(int(q[1])):
                temp += ans.popleft()
            print(temp)
            num -= int(q[1])
    return

if __name__ == '__main__':
    main()