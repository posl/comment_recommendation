def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for a in A:
            if a % 2 == 1:
                count += 1
        print(count)
