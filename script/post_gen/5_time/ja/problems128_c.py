Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M=map(int,input().split())
    k=[0]*M
    s=[0]*M
    p=[0]*M
    for i in range(M):
        k[i],*s[i]=map(int,input().split())
    p=list(map(int,input().split()))
    ans=0
    for i in range(2**N):
        for j in range(M):
            cnt=0
            for l in range(k[j]):
                if (i>>(s[j][l]-1))&1:
                    cnt+=1
            if cnt%2==p[j]:
                if j==M-1:
                    ans+=1
            else:
                break
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    k = []
    s = []
    p = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        s.append(k[i][1:])
    p = list(map(int, input().split()))

    ans = 0
    for i in range(2 ** n):
        flag = True
        for j in range(m):
            on = 0
            for l in range(k[j][0]):
                if (i >> s[j][l] - 1) & 1:
                    on += 1
            if on % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    k = []
    s = []
    for i in range(M):
        tmp = list(map(int,input().split()))
        k.append(tmp[0])
        s.append(tmp[1:])
    p = list(map(int,input().split()))
    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            tmp = 0
            for l in s[j]:
                if (i>>(l-1))&1:
                    tmp += 1
            if tmp%2 != p[j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    K = []
    S = []
    for i in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            count = 0
            for k in range(K[j]):
                if i >> (S[j][k] - 1) & 1:
                    count += 1
            if count % 2 != P[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def check_light(light, switch):
    #lightのスイッチの数だけforを回す
    for i in range(light[0]):
        #もしスイッチがonならcountを1増やす
        if s[light[i+1]-1] == 1:
            count += 1
    #countがlightの数の半分より大きいならばTrueを返す
    if count > light[0]//2:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    K = [0] * M
    S = [0] * M
    for i in range(M):
        K[i], *S[i] = map(int, input().split())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        cnt = 0
        for j in range(M):
            cnt2 = 0
            for k in range(K[j]):
                if i & (1 << (S[j][k] - 1)):
                    cnt2 += 1
            if cnt2 % 2 == P[j]:
                cnt += 1
        if cnt == M:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    s = [None]*M
    for i in range(M):
        s[i] = list(map(int,input().split()))
    p = list(map(int,input().split()))

    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            count = 0
            for k in range(1,s[j][0]+1):
                if i & (1<<(s[j][k]-1)):
                    count += 1
            if count % 2 != p[j]:
                flag = False
        if flag:
            ans += 1

    print(ans)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    l = []
    for i in range(M):
        l.append(list(map(int,input().split())))
    p = list(map(int,input().split()))

    #print(l)
    #print(p)

    #電球の個数
    light = 0
    #スイッチのon/offの組み合わせ
    count = 0

    #電球の個数を数える
    for i in range(M):
        light += l[i][0]

    #スイッチのon/offの組み合わせを数える
    for i in range(2**N):
        #on/offの組み合わせをlistにする
        on_off = list(format(i,'0{}b'.format(N)))
        #print(on_off)

        #電球の個数分だけループ
        for j in range(M):
            #電球の個数分のスイッチをループ
            for k in range(1,l[j][0]+1):
                #print(on_off[l[j][k]-1])
                #スイッチがonの時
                if on_off[l[j][k]-1] == '1':
                    count += 1
            #print(count)
            #print(p[j])
            #スイッチのonの個数が奇数個の時
            if count % 2 == 1:
                #print('奇数')
                #電球が点灯している時
                if p[j] == 1:
                    count = 0
                #電球が点灯していない時
                else:
                    count = 0
                    break
            #スイッチのonの個数が偶数個の時
            else:
                #print('偶数')
                #電球が点灯している時
                if p[j] == 0:
                    count = 0
                #電球が点灯していない時
                else:
                    count = 0
                    break

        #print(count)
        #print(light)
        #電球の

=======
Suggestion 10

def check_light(light, on_off):
    cnt = 0
    for i in light[1:]:
        if on_off[i-1] == 1:
            cnt += 1
    if cnt % 2 == light[0]:
        return True
    else:
        return False
