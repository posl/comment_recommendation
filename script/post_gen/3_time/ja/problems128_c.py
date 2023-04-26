Synthesizing 10/10 solutions

=======
Suggestion 1

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
        light = [0] * M
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M):
                    if j + 1 in S[k]:
                        light[k] += 1
        for j in range(M):
            if light[j] % 2 != P[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    K = []
    S = []
    for _ in range(M):
        k, *s = map(int, input().split())
        K.append(k)
        S.append(s)
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(K[j]):
                if (i >> (S[j][k] - 1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    k = []
    s = []
    for i in range(m):
        a = list(map(int,input().split()))
        k.append(a[0])
        s.append(a[1:])
    p = list(map(int,input().split()))

    ans = 0
    for i in range(2**n):
        flag = True
        for j in range(m):
            cnt = 0
            for l in range(k[j]):
                if i&(2**(s[j][l]-1)):
                    cnt += 1
            if cnt%2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 4

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
    for i in range(2**n):
        flag = True
        for j in range(m):
            count = 0
            for l in range(k[j][0]):
                if (i>>(s[j][l]-1)) & 1:
                    count += 1
            if count % 2 != p[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = []
    for i in range(M):
        S.append(list(map(int, input().split())))
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(1, len(S[j])):
                if (i >> (S[j][k] - 1)) & 1:
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    ans = 0
    for i in range(1<<N):
        flag = True
        for j in range(M):
            cnt = 0
            for k in range(1, S[j][0]+1):
                if i & (1<<(S[j][k]-1)):
                    cnt += 1
            if cnt % 2 != P[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 7

def check_light(lights, switches, p):
    for i in range(len(lights)):
        count = 0
        for j in range(1, len(switches[i])):
            if lights[switches[i][j]-1] == 1:
                count += 1
        if count % 2 != p[i]:
            return False
    return True

=======
Suggestion 8

def checkLight(switch, light):
    for i in range(len(light)):
        count = 0
        for j in range(1, len(light[i])):
            if switch[light[i][j] - 1] == 1:
                count += 1
        if count % 2 != light[i][0]:
            return False
    return True

=======
Suggestion 9

def check(ary, p):
  for i in range(len(ary)):
    if ary[i] % 2 != p[i]:
      return False
  return True

=======
Suggestion 10

def get_switch_state( switch_state, switch_count, switch_list, bulb_list, bulb_state, bulb_count, bulb_index ):
    if bulb_index == bulb_count:
        bulb_state_list = [ 0 for i in range( bulb_count ) ]
        for i in range( bulb_count ):
            for j in bulb_list[i]:
                bulb_state_list[i] += switch_state[j-1]
            bulb_state_list[i] %= 2
        if bulb_state_list == bulb_state:
            return 1
        else:
            return 0
    else:
        switch_state[ switch_list[bulb_index][switch_count[bulb_index]] - 1 ] = 0
        result = get_switch_state( switch_state, switch_count, switch_list, bulb_list, bulb_state, bulb_count, bulb_index + 1 )
        switch_state[ switch_list[bulb_index][switch_count[bulb_index]] - 1 ] = 1
        result += get_switch_state( switch_state, switch_count, switch_list, bulb_list, bulb_state, bulb_count, bulb_index + 1 )
        return result
