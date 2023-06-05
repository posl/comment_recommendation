Synthesizing 10/10 solutions

=======
Suggestion 1

def check(n, l):
    for i in range(n):
        if l[i] % 2 == 0:
            if l[i] % 3 != 0 and l[i] % 5 != 0:
                return False
    return True

n = int(input())
l = list(map(int, input().split()))
print("APPROVED" if check(n, l) else "DENIED")

=======
Suggestion 2

def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                print('DENIED')
                return
    print('APPROVED')
main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if (i % 2 == 0) and (i % 3 != 0) and (i % 5 != 0):
            print('DENIED')
            return
    print('APPROVED')

=======
Suggestion 5

def check_condition(n, a):
  for i in range(n):
    if a[i] % 2 == 0 and (a[i] % 3 != 0 and a[i] % 5 != 0):
      return False
  return True

=======
Suggestion 6

def judge(s):
    if s % 3 == 0 or s % 5 == 0:
        return True
    else:
        return False

n = int(input())
l = list(map(int, input().split()))

flag = True
for i in l:
    if i % 2 == 0:
        if judge(i) == False:
            flag = False
            break

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print("APPROVED" if all(x % 2 == 1 or x % 3 == 0 or x % 5 == 0 for x in a) else "DENIED")

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    flag = True
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                flag = False
                break
    if flag:
        print('APPROVED')
    else:
        print('DENIED')

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    r = 'APPROVED'
    for i in a:
        if i % 2 == 0:
            if i % 3 != 0 and i % 5 != 0:
                r = 'DENIED'
                break
    print(r)

=======
Suggestion 10

def main():
    n = int(input())
    nums = list(map(int,input().split()))
    for num in nums:
        if num % 2 == 0:
            if num % 3 != 0 and num % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")
