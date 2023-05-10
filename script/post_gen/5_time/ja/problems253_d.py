Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, A, B = map(int, input().split())
g = gcd(A, B)
print(N - N // A - N // B + N // (A * B // g))

=======
Suggestion 4

def main():
    N, A, B = map(int, input().split())
    print(sum([x for x in range(1, N+1) if x % A != 0 and x % B != 0]))

=======
Suggestion 5

def main():
    N,A,B = map(int,input().split())
    #print(N,A,B)
    #print(N//A)
    #print(N//B)
    #print(N//(A*B))
    print(N-(N//A+N//B-N//(A*B))*2)
    return

=======
Suggestion 6

def main():
    N,A,B = map(int,input().split())

    # 1~Nまでの和
    sumN = N*(N+1)//2

    # Aの倍数の和
    sumA = A*(N//A)*((N//A)+1)//2

    # Bの倍数の和
    sumB = B*(N//B)*((N//B)+1)//2

    # AとBの公倍数の和
    sumAB = (A*B)*((N//(A*B))+1)//2

    print(sumN - sumA - sumB + sumAB)

=======
Suggestion 7

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

n,a,b=map(int,input().split())
lcm=a*b//gcd(a,b)
ans=n//a+n//b-n//lcm
print(ans)

=======
Suggestion 8

def lcm(a,b):
    return a*b//gcd(a,b)

=======
Suggestion 9

def problem253_d():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    #print((N // A) * A, (N // B) * B)
    #print((N // A) * A + (N // B) * B)
    #print((N // A) * A + (N // B) * B - (N // (A*B)) * (A*B))
    print(N * (N + 1) // 2 - (N // A) * (A * (1 + N // A)) // 2 - (N // B) * (B * (1 + N // B)) // 2 + (N // (A * B)) * ((A * B) * (1 + N // (A * B))) // 2)
