def main():
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #n = int(input())
    #a = list(map(int, input().split()))
    count = 0
    while n > 0:
        n -= k-1
        count += 1
    print(count)
