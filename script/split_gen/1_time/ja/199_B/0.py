def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(min(A), max(B) + 1):
        if min(A) <= i <= max(B):
            count += 1
    print(count)
