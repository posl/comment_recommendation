Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    for a,b in ab:
        if a > k:
            break
        k += b
    print(k)

=======
Suggestion 2

def main():
    # 读入数据
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # AB.sort(key=lambda x: x[0])
    # print(AB)
    # 处理数据
    AB.sort(key=lambda x: x[0])
    # print(AB)
    for i in range(N):
        if K >= AB[i][0]:
            K += AB[i][1]
        else:
            break
    # 输出结果
    print(K)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(k)
    #print(n)
    i = 0
    while k > 0:
        #print(a[i])
        if k >= a[i]:
            k -= a[i]
            k += b[i]
            i += 1
        else:
            break
        if i == n:
            break
    print(k)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    money = k
    for i in range(n):
        if money < ab[i][0]:
            print(money)
            return
        money += ab[i][1]
    print(money)

=======
Suggestion 5

def main():
    # 读取数据
    n,k = map(int,input().split())
    #print(n,k)
    #print(type(n),type(k))
    #print(n)
    #print(k)
    #print(type(n))
    #print(type(k))
    #print(type(int(n)),type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))

    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))

    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))

    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))

    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k)))

    #print(type(int(n)))
    #print(type(int(k)))
    #print(int(n))
    #print(int(k))
    #print(type(int(n)))
    #print(type(int(k

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    money = K
    village = 0
    for i in range(N):
        if money >= AB[i][0] - village:
            money += AB[i][1]
            village = AB[i][0]
        else:
            break
    print(village + money)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        friends.append(list(map(int, input().split())))
    friends.sort()
    for friend in friends:
        if friend[0] <= K:
            K += friend[1]
        else:
            break
    print(K)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    # 朋友村庄
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    # print(AB)
    # 朋友村庄到达的最大村庄
    max_village = 0
    # 朋友村庄的朋友村庄
    AB2 = []
    for i in range(N):
        if AB[i][0] > max_village + 1:
            break
        # 朋友村庄的朋友村庄
        AB2.append(AB[i])
        max_village = max(max_village, AB[i][0] + AB[i][1])
    # print(AB2)
    # 朋友村庄的朋友村庄的朋友村庄
    AB3 = []
    for i in range(len(AB2)):
        if AB2[i][0] > max_village + 1:
            break
        # 朋友村庄的朋友村庄的朋友村庄
        AB3.append(AB2[i])
        max_village = max(max_village, AB2[i][0] + AB2[i][1])
    # print(AB3)
    # 朋友村庄的朋友村庄的朋友村庄的朋友村庄
    AB4 = []
    for i in range(len(AB3)):
        if AB3[i][0] > max_village + 1:
            break
        # 朋友村庄的朋友村庄的朋友村庄的朋友村庄
        AB4.append(AB3[i])
        max_village = max(max_village, AB3[i][0] + AB3[i][1])
    # print(AB4)
    # 朋友村庄的朋友村庄的朋友村庄的朋友村庄的朋友村庄
    AB

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    villagelist = []
    for i in range(N):
        A, B = map(int, input().split())
        villagelist.append([A, B])
    villagelist.sort()
    sum = 0
    for i in range(N):
        if villagelist[i][0] - sum <= K:
            K -= villagelist[i][0] - sum
            sum = villagelist[i][0]
            K += villagelist[i][1]
        else:
            print(sum + K)
            exit()
    print(sum + K)

=======
Suggestion 10

def main():
    n,k=map(int,input().split())
    a=[]
    b=[]
    for i in range(n):
        ai,bi=map(int,input().split())
        a.append(ai)
        b.append(bi)
    index=0
    while index<n and k>=a[index]:
        k+=b[index]
        index+=1
    print(k)
