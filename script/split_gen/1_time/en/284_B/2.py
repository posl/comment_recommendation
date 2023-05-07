def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(sum([1 for a in A if a % 2 == 1]))
main()
