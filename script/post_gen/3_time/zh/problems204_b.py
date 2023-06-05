Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    num = int(input())
    nuts = input().split()
    nuts = list(map(int, nuts))
    count = 0
    for i in range(num):
        if nuts[i] > 10:
            count += nuts[i] - 10
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if a[i] >= 10:
            s += a[i] - 10
    print(s)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)

=======
Suggestion 4

def getNutsCount(nuts):
    nutsCount = 0
    for nut in nuts:
        if nut > 10:
            nutsCount += nut - 10
    return nutsCount

=======
Suggestion 5

def harvest_nuts(num_nuts):
    nuts = []
    for i in range(num_nuts):
        nuts.append(int(input()))
    nuts.sort()
    nuts.reverse()
    total_nuts = 0
    for i in range(num_nuts):
        if nuts[i] >= 10:
            total_nuts += nuts[i] - 10
    return total_nuts

=======
Suggestion 6

def get_nuts(nuts):
    nuts_sum = 0
    for i in nuts:
        if i > 10:
            nuts_sum += i - 10
    return nuts_sum

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in a:
        if i > 10:
            ans += i - 10
    print(ans)

=======
Suggestion 8

def main():
	n = int(input())
	trees = [int(i) for i in input().split()]
	
	count = 0
	for tree in trees:
		if tree > 10:
			count += tree - 10
	print(count)

=======
Suggestion 9

def get_nuts(nuts):
    nuts.sort(reverse=True)
    nuts = nuts[10:]
    return sum(nuts)
