Synthesizing 10/10 solutions

=======
Suggestion 1

def isTriangle(a,b,c):
    if a < b + c and b < c + a and c < a + b:
        return True
    else:
        return False

=======
Suggestion 2

def count_triangle():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    count += 1
                else:
                    break
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    count += 1
                else:
                    break
    print(count)

=======
Suggestion 4

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

=======
Suggestion 5

def get_triangles(nums):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] > nums[k]:
                    count += 1
    return count

=======
Suggestion 6

def judge(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

n = int(input())
l = list(map(int,input().split()))
l.sort()

count = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if judge(l[i],l[j],l[k]):
                count += 1

print(count)

=======
Suggestion 7

def count_triangle(n, l):
    l.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    count += 1
                else:
                    break
    return count

=======
Suggestion 8

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    ans += 1
    print(ans)

=======
Suggestion 9

def calc_triangle_num(L):
    L.sort()
    num = 0
    for i in range(0, len(L) - 2):
        for j in range(i + 1, len(L) - 1):
            for k in range(j + 1, len(L)):
                if L[i] + L[j] > L[k]:
                    num += 1
                else:
                    break
    return num

=======
Suggestion 10

def get_triangle_count(stick_list):
    triangle_count = 0
    stick_list.sort()
    for a_index in range(0, len(stick_list) - 2):
        for b_index in range(a_index + 1, len(stick_list) - 1):
            for c_index in range(b_index + 1, len(stick_list)):
                if stick_list[a_index] + stick_list[b_index] > stick_list[c_index]:
                    triangle_count += 1
    return triangle_count
