Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = map(int, raw_input().split())
    cnt = 0
    while cnt < 3:
        cnt += 1
        a = a[a[0]]
    print a[0]

=======
Suggestion 2

def main():
    a = input()
    a = a.split()
    b = 0
    for i in range(3):
        b = a[b]
        b = int(b)
    print(b)

=======
Suggestion 3

def main():
    a = map(int, raw_input().split())
    for i in range(10):
        a[i] = a[a[i]]
    print a[0]

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 5

def main():
    a = input().split()
    k = 0
    for i in range(3):
        k = int(a[k])
    print(k)

=======
Suggestion 6

def main():
    import sys
    a = [int(x) for x in sys.stdin.readline().strip().split()]
    b = [0] * 10
    for i in range(10):
        b[a[i]] = i
    p = 0
    for i in range(3):
        p = b[p]
    print(p)
main()

=======
Suggestion 7

def main():
    arr = list(map(int, input().split()))
    count = 0
    while True:
        count += 1
        if count > 100:
            break
        arr[0] = arr[arr[0]]
        if arr[0] == 0:
            break
    print(arr[0])

=======
Suggestion 8

def main():
    input_str = input()
    input_list = input_str.split()
    input_list = list(map(int, input_list))
    count = 0
    while count < 3:
        input_list = list(map(lambda x:input_list[x], input_list))
        count += 1
    print(input_list[0])

=======
Suggestion 9

def main():
    a = map(int, raw_input().split())
    i = 0
    while i < 3:
        a = a[a[i]]
        i += 1
    print a

=======
Suggestion 10

def main():
    a = input()
    a = a.split(' ')
    for i in range(10):
        a[i] = int(a[i])
    k = 0
    for i in range(3):
        k = a[k]
    print(k)
