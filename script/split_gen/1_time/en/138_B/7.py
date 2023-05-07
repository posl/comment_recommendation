def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(sum([1/a for a in A])**-1)
