Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    print(int(k/2 * (k-k/2)))

=======
Suggestion 2

def problem108_a():
    K = int(input())
    print(K//2*(K-K//2))

=======
Suggestion 3

def main():
    k = int(input())
    count = 0
    for i in range(1, k + 1):
        if i % 2 == 0:
            for j in range(1, k + 1):
                if j % 2 == 1:
                    count += 1
        else:
            for j in range(1, k + 1):
                if j % 2 == 0:
                    count += 1
    print(count)

=======
Suggestion 4

def get_even_odd_pair_count(k):
    even_count = (k // 2) + (k % 2)
    odd_count = k // 2
    return even_count * odd_count

=======
Suggestion 5

def fun(k):
    sum=0
    for i in range(1,k+1):
        if i%2==0:
            for j in range(1,k+1):
                if j%2==1:
                    sum+=1
    return sum

k=int(input())
print(fun(k))

=======
Suggestion 6

def main():
    K = int(input())
    if K < 2 or K > 100:
        print("K must between 2 and 100")
        return
    result = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            if i % 2 == 0 and j % 2 == 1:
                result += 1
    print(result)

=======
Suggestion 7

def main():
    k = int(input())
    print(int((k+1)/2)**2)
