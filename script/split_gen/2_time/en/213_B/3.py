def main():
    N = int(input())
    A = list(map(int,input().split()))
    min_a = min(A)
    A.remove(min_a)
    print(A.index(min(A))+1)
main()
