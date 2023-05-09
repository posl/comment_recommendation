def main():
    S = input()
    from collections import deque
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        cost, num, index = queue.popleft()
        if num > int(S):
            continue
        if num == int(S):
            print(cost)
            return
        if index < len(S):
            queue.append((cost+1, num*10 + int(S[index]), index+1))
            queue.append((cost+1, num, index+1))

if __name__ == '__main__':
    main()