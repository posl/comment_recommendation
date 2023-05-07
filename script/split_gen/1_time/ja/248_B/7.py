def main():
    A,B,K = map(int,input().split())
    count = 0
    while True:
        if count == K:
            break
        if A % 2 == 1:
            A = A - 1
        A = A / 2
        B = B + A
        count = count + 1
    print(int(A),int(B))
