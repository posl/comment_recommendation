Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(N)]
    ab.sort()
    money = K
    village = 0
    for i in range(N):
        if money >= ab[i][0] - village:
            money += ab[i][1]
            village = ab[i][0]
        else:
            break
    village += money
    print(village)

main()

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    array = []
    for i in range(n):
        a, b = map(int, input().split())
        array.append((a, b))
    array.sort()

    money = k
    for i in range(n):
        if money >= array[i][0]:
            money += array[i][1]

    print(money)

main()

=======
Suggestion 3

def solve(n, k, ab):
    ab.sort(key=lambda x: x[0])
    for a, b in ab:
        if k < a:
            break
        k += b
    return k

=======
Suggestion 4

def solve(N, K, AB):
    AB.sort(key=lambda x: x[0])
    for i in range(N):
        if K >= AB[i][0]:
            K += AB[i][1]
        else:
            break
    return K

=======
Suggestion 5

def main():
    n,k=map(int,input().split())
    ab=[list(map(int,input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    #print(ab)
    money=k
    now=0
    for i in range(n):
        if money>=ab[i][0]-now:
            money+=ab[i][1]
            now=ab[i][0]
        else:
            break
    print(now+money)
main()

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    for a,b in ab:
        if k < a:
            break
        k += b
    print(k)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        a, b = map(int, input().split())
        friends.append([a, b])
    friends.sort()
    last = 0
    for i in range(n):
        if friends[i][0] - last <= k:
            k -= friends[i][0] - last
            k += friends[i][1]
            last = friends[i][0]
        else:
            print(last + k)
            return
    print(last + k)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    friends = []
    for i in range(n):
        friends.append(list(map(int, input().split())))
    friends.sort(key=lambda x: x[0])
    friends.append([10**100, 0])
    money = k
    village = 0
    for i in range(n):
        if money >= friends[i][0] - village:
            money -= friends[i][0] - village
            money += friends[i][1]
            village = friends[i][0]
        else:
            break
    village += money
    print(village)

=======
Suggestion 9

def main():
    # 读取数据
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照村庄编号升序排序
    ab.sort()

    # 计算最后一村的编号
    village = 0
    for a, b in ab:
        if k < a - village:
            break
        k += b - (a - village)
        village = a

    # 输出结果
    print(village + k)

=======
Suggestion 10

def solve(n, k, ab):
    ab.sort(key=lambda x: x[0])
    for a, b in ab:
        if k < a:
            break
        else:
            k += b
    return k
