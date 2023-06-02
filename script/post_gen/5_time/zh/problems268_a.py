Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    num_list = list(map(int, input().split()))
    print(len(set(num_list)))

=======
Suggestion 2

def main():
    a,b,c,d,e = map(int,input().split())
    arr = [a,b,c,d,e]
    arr.sort()
    count = 1
    for i in range(1,5):
        if arr[i] != arr[i-1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    input_str = input()
    input_list = input_str.split()
    input_list = list(map(int, input_list))
    input_set = set(input_list)
    print(len(input_set))

=======
Suggestion 4

def main():
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()
    list = [a, b, c, d, e]
    list = set(list)
    print(len(list))

main()

=======
Suggestion 5

def main():
    input = raw_input()
    nums = input.split(' ')
    nums = map(int, nums)
    print len(set(nums))

=======
Suggestion 6

def main():
    nums = input().split()
    nums = [int(x) for x in nums]
    print(len(set(nums)))

=======
Suggestion 7

def main():
    nums = list(map(int, input().strip().split()))
    print(len(set(nums)))

=======
Suggestion 8

def main():
    a, b, c, d, e = map(int, input().split())
    nums = [a, b, c, d, e]
    print(len(set(nums)))

=======
Suggestion 9

def main():
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 10

def main():
    a,b,c,d,e=map(int,input().split())
    print(len(set([a,b,c,d,e])))
