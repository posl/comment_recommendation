def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([a-10 for a in A if a>10]))
main()
