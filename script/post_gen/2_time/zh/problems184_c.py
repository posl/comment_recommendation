Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    # 计算
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) == 3:
                if r1 + i + c1 + j == r2 + c2 or r1 + i - c1 - j == r2 - c2 or abs(r1 + i - r2) + abs(c1 + j - c2) <= 3:
                    print(2)
                    return
    print(3)
    return

=======
Suggestion 2

def main():
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2)+abs(c1-c2) <= 3:
        print(1)
        return
    if (r1+c1)%2 == (r2+c2)%2 or abs(r1-r2)+abs(c1-c2) <= 6 or abs(r1+c1-r2-c2) <= 3 or abs(r1-c1-r2+c2) <= 3:
        print(2)
        return
    print(3)

=======
Suggestion 3

def main():
    r_1, c_1 = map(int, input().split())
    r_2, c_2 = map(int, input().split())
    if r_1 == r_2 and c_1 == c_2:
        print(0)
        return
    if abs(r_1 - r_2) + abs(c_1 - c_2) <= 3:
        print(1)
        return
    if r_1 + c_1 == r_2 + c_2:
        print(1)
        return
    if r_1 - c_1 == r_2 - c_2:
        print(1)
        return
    if (r_1 + c_1) % 2 == (r_2 + c_2) % 2:
        print(2)
        return
    if abs(r_1 - r_2) + abs(c_1 - c_2) <= 6:
        print(2)
        return
    if abs((r_1 + c_1) - (r_2 + c_2)) <= 3:
        print(2)
        return
    if abs((r_1 - c_1) - (r_2 - c_2)) <= 3:
        print(2)
        return
    print(3)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) <= 3:
                if (r1 + i + c1 + j) % 2 == (r2 + c2) % 2:
                    print(2)
                    return
    print(3)

=======
Suggestion 6

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if (r1, c1) == (r2, c2):
        print(0)
        return
    if (r1 + c1) == (r2 + c2) or (r1 - c1) == (r2 - c2) or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) != 3:
                continue
            x = r1 + i
            y = c1 + j
            if (x + y) == (r2 + c2) or (x - y) == (r2 - c2):
                print(2)
                return
    print(3)
    return

=======
Suggestion 7

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if (r1, c1) == (r2, c2):
        print(0)
        return

    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return

    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return

    for dr in range(-3, 4):
        for dc in range(-3, 4):
            if abs(dr) + abs(dc) != 3:
                continue
            nr, nc = r1 + dr, c1 + dc
            if abs(nr - r2) + abs(nc - c2) <= 3:
                print(2)
                return

    print(3)

=======
Suggestion 8

def bfs(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0
    visited = set()
    visited.add((r1, c1))
    queue = [(r1, c1)]
    step = 0
    while queue:
        step += 1
        for _ in range(len(queue)):
            r, c = queue.pop(0)
            for i in range(-3, 4):
                for j in range(-3, 4):
                    if (r + i, c + j) not in visited:
                        if r + i == r2 and c + j == c2:
                            return step
                        if r + i + c + j == r2 + c2 or r + i - c - j == r2 - c2 or abs(r + i - r2) + abs(c + j - c2) <= 3:
                            visited.add((r + i, c + j))
                            queue.append((r + i, c + j))
    return -1

=======
Suggestion 9

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if i == 0 or j == 0:
                continue
            if abs(i) + abs(j) <= 3:
                if r1 + i + c1 + j == r2 + c2 or r1 + i - c1 - j == r2 - c2 or abs(r1 + i - r2) + abs(c1 + j - c2) <= 6:
                    print(2)
                    return
    print(3)
    return

=======
Suggestion 10

def main():
    input_list = []
    for i in range(2):
        input_list.append(list(map(int, input().split())))
    r1, c1 = input_list[0][0], input_list[0][1]
    r2, c2 = input_list[1][0], input_list[1][1]
    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        exit()
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        exit()
    print(2)
