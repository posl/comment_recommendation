def main():
    A, B, K = map(int, input().split())
    count = 0
    for i in range(1, max(A,B)+1):
        if A % i == 0 and B % i == 0:
            count += 1
        if count == K:
            print(i)
            break
