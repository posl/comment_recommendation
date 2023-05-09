def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0]*n
    for i in a:
        count[i-1] += 1
    for i in count:
        print(i)
