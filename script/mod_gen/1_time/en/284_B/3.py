def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        print(sum(1 for x in A if x % 2 == 1))
main()
