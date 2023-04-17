Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    K = int(input())
    even = [i for i in range(2, K+1, 2)]
    odd = [i for i in range(1, K+1, 2)]
    print(len(even)*len(odd))

main()

=======

def main():
    k = int(input())
    ans = 0
    for i in range(1,k+1):
        if i % 2 == 0:
            ans += (k-i) // 2 + 1
    print(ans)

=======

def main():
    K = int(input())
    cnt = 0
    for i in range(1,K+1):
        if i % 2 == 0:
            cnt += (K-i)//2+1
    print(cnt)

main()

=======

def main():
    k = int(input())
    even = k // 2
    odd = (k+1) // 2
    print(even * odd)

=======

def main():
    k = int(input())
    even = k // 2
    odd = k - even
    print(even * odd)

=======

def main():
    K = int(input())
    print(int(K/2)*int((K+1)/2))

=======

def main():
    K = int(input())
    print((K//2)*(K//2 + K%2))

=======

def main():
    K = int(input())
    print(K*(K-1)//2)

=======

def main():
    K = int(input())
    print(int(K/2)*(int(K/2)+1))
