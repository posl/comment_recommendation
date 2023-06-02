Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = sum(a[-k:])
    print(s)

=======
Suggestion 2

def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    # 求解
    # 每个部门的人数
    department = [0] * n
    for i in range(n):
        department[a[i] - 1] += 1
    # 每个部门的人数对应的部门数
    count = [0] * n
    for i in range(n):
        count[department[i] - 1] += 1
    # 部门数
    department_num = n
    # 项目数
    project_num = 0
    # 从部门数最多的部门开始
    for i in range(n - 1, -1, -1):
        # 如果部门数为0，结束
        if department_num == 0:
            break
        # 如果部门人数为0，跳过
        if count[i] == 0:
            continue
        # 如果部门人数不足，结束
        if count[i] < k:
            break
        # 计算项目数
        project_num += count[i] // k
        # 减少部门数
        department_num -= count[i]
        # 减少部门人数
        count[i - 1] += count[i] % k
    # 输出
    print(project_num)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n-k):
        ans += a[i]
    print(ans)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i < k:
            continue
        ans += a[i]
    print(ans)
main()

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n - k + 1):
        ans = max(ans, a[i + k - 1] - a[i])
    print(ans + 1)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a)
    i = 0
    j = k - 1
    ans = 0
    while j < n:
        ans += 1
        i += k
        j += k
        while j < n and a[i] == a[j]:
            i += 1
            j += 1
    print(ans)

=======
Suggestion 7

def get_max_project_num(n, k, a):
    a.sort()
    i = 0
    j = 0
    count = 0
    while i < n and j < n:
        if a[j] - a[i] + 1 > k:
            i += 1
        else:
            count += 1
            j += 1
    return count

=======
Suggestion 8

def problems227_d(n,k,alist):
    alist.sort()
    print(alist)
    count = 0
    for i in range(0,n-k,k):
        count = count + 1
    print(count)
    return count

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    dic = {}
    for i in range(n):
        if a[i] in dic:
            dic[a[i]] = dic[a[i]] + 1
        else:
            dic[a[i]] = 1
    #print(dic)
    #print(a)
    #print(n,k)
    ans = 0
    for i in range(n):
        if dic[a[i]] >= k:
            ans = ans + 1
            dic[a[i]] = dic[a[i]] - k
        else:
            k = k - dic[a[i]]
            dic[a[i]] = 0
    print(ans)
