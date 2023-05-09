Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    if k % 2 == 0:
        print(int(k/2)**2)
    else:
        print(int(k/2)*(int(k/2)+1))

=======
Suggestion 2

def main():
    k = int(input())
    if k % 2 == 0:
        print(int((k/2))**2)
    else:
        print(int((k/2)) * (int((k/2)) + 1))

=======
Suggestion 3

def solve(K):
    ans = 0
    for i in range(1, K+1):
        for j in range(i+1, K+1):
            if i%2 != j%2:
                ans += 1
    return ans

=======
Suggestion 4

def main():
    k = int(input())
    if k % 2 == 0:
        print((k//2)**2)
    else:
        print(((k+1)//2)**2)

=======
Suggestion 5

def count_pairs(number):
    count = 0
    for i in range(1, number+1):
        if i % 2 == 0:
            continue
        for j in range(1, number+1):
            if j % 2 == 1:
                continue
            count += 1
    return count

print(count_pairs(int(input())))

=======
Suggestion 6

def main():
    k = int(input())
    if k%2 == 0:
        print((k/2)**2)
    else:
        print(int((k/2)*(k/2+1)))

=======
Suggestion 7

def main():
    k = int(input())
    #print(k)
    if k%2 == 0:
        print((k//2)**2)
    else:
        print((k//2)*(k//2+1))

=======
Suggestion 8

def main():
    K = int(input())
    print(int((K/2)*(K/2 + K%2)))

main()

=======
Suggestion 9

def find_ways_to_choose_pair(k):
    return int(k/2) * int(k/2 + k%2)

k = int(input())

print(find_ways_to_choose_pair(k))

=======
Suggestion 10

def get_input():
    import sys
    return int(sys.stdin.readline().rstrip())
