Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = [0] + a
    b = [0] + b
    #print(a)
    #print(b)
    #print(n,m,k)
    #print(a[1])
    #print(b[2])
    #print(a[1] + b[2])
    ans = 0
    a_sum = 0
    b_sum = 0
    a_i = 0
    b_i = 0
    for i in range(1,n+1):
        a_sum += a[i]
        if a_sum > k:
            a_i = i - 1
            break
        else:
            a_i = i
    for j in range(1,m+1):
        b_sum += b[j]
        if b_sum > k:
            b_i = j - 1
            break
        else:
            b_i = j
    #print(a_i)
    #print(b_i)
    ans = max(a_i,b_i)
    #print(ans)
    a_sum = 0
    b_sum = 0
    for i in range(1,a_i+1):
        for j in range(1,b_i+1):
            if a_sum + b_sum + a[i] + b[j] > k:
                break
            else:
                ans = max(ans,i+j)
                b_sum += b[j]
        a_sum += a[i]
        b_sum = 0
    print(ans)

=======
Suggestion 2

def solve():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.append(0)
    b.append(0)
    for i in range(1,n+1):
        a[i] += a[i-1]
    for i in range(1,m+1):
        b[i] += b[i-1]
    ans = 0
    j = m
    for i in range(n+1):
        if a[i] > k:
            break
        while a[i] + b[j] > k:
            j -= 1
        ans = max(ans,i+j)
    print(ans)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    n,m,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.insert(0,0)
    b.insert(0,0)
    for i in range(1,n+1):
        a[i] += a[i-1]
    for i in range(1,m+1):
        b[i] += b[i-1]
    ans = 0
    j = m
    for i in range(n+1):
        if a[i] > k:
            break
        while a[i] + b[j] > k:
            j -= 1
        ans = max(ans, i+j)
    print(ans)

=======
Suggestion 5

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = [0]*(n+1)
    b_sum = [0]*(m+1)
    for i in range(n):
        a_sum[i+1] = a_sum[i] + a[i]
    for i in range(m):
        b_sum[i+1] = b_sum[i] + b[i]
    ans = 0
    j = m
    for i in range(n+1):
        if a_sum[i] > k:
            break
        while b_sum[j] > k - a_sum[i]:
            j -= 1
        ans = max(ans,i+j)
    print(ans)

=======
Suggestion 6

def main():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum + b_sum <= k:
        print(n+m)
        return
    a_sum = 0
    b_sum = 0
    a_index = 0
    b_index = 0
    count = 0
    while a_sum + b_sum <= k:
        if a_sum < b_sum:
            a_sum += a[a_index]
            a_index += 1
        else:
            b_sum += b[b_index]
            b_index += 1
        count += 1
        if a_index == n or b_index == m:
            break
    if a_sum + b_sum <= k:
        print(n+m)
        return
    if a_sum < b_sum:
        b_sum -= b[b_index - 1]
        b_index -= 1
    else:
        a_sum -= a[a_index - 1]
        a_index -= 1
    count -= 1
    while a_index >= 0 and b_index >= 0:
        if a_sum < b_sum:
            a_sum += a[a_index]
            a_index -= 1
        else:
            b_sum += b[b_index]
            b_index -= 1
        count += 1
    print(count)

=======
Suggestion 7

def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(n - 1):
        a[i + 1] += a[i]
    for i in range(m - 1):
        b[i + 1] += b[i]

    ans = 0
    j = m
    for i in range(n + 1):
        if a[i] > k:
            break
        while j > 0 and a[i] + b[j - 1] > k:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

=======
Suggestion 8

def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 累计和
    for i in range(1, n):
        a[i] += a[i - 1]
    for i in range(1, m):
        b[i] += b[i - 1]

    ans = 0
    j = m - 1
    for i in range(n):
        if a[i] > k:
            break
        while j >= 0 and a[i] + b[j] > k:
            j -= 1
        ans = max(ans, i + j + 2)

    print(ans)

=======
Suggestion 9

def solve():
    # n,m,k = map(int,input().split())
    # a = list(map(int,input().split()))
    # b = list(map(int,input().split()))
    # a.sort()
    # b.sort()
    # time = 0
    # count = 0
    # while time <= k:
    #     if time+a[0] < time+b[0]:
    #         if time+a[0] <= k:
    #             count += 1
    #             time += a[0]
    #             a.pop(0)
    #         else:
    #             return count
    #     else:
    #         if time+b[0] <= k:
    #             count += 1
    #             time += b[0]
    #             b.pop(0)
    #         else:
    #             return count
    # return count
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    time = 0
    count = 0
    while time <= k:
        if len(a) == 0:
            if time+b[0] <= k:
                count += 1
                time += b[0]
                b.pop(0)
            else:
                return count
        elif len(b) == 0:
            if time+a[0] <= k:
                count += 1
                time += a[0]
                a.pop(0)
            else:
                return count
        else:
            if a[0] < b[0]:
                if time+a[0] <= k:
                    count += 1
                    time += a[0]
                    a.pop(0)
                else:
                    return count
            else:
                if time+b[0] <= k:
                    count += 1
                    time += b[0]
                    b.pop(0)
                else:
                    return count
    return count

print(solve())
