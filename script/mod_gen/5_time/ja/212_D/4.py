def main():
    import sys
    input = sys.stdin.readline
    from collections import deque
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    ans = deque()
    bag = deque()
    min_num = 0
    for i in range(Q):
        if query[i][0] == '1':
            bag.append(int(query[i][1]))
        elif query[i][0] == '2':
            min_num += int(query[i][1])
        else:
            ans.append(min_num+bag.popleft())
            min_num -= ans[-1]
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()