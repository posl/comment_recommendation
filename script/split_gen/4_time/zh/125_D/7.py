def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [abs(i) for i in a]
    c = [i for i in a if i < 0]
    if len(c) % 2 == 0:
        print(sum(b))
    else:
        print(sum(b) - 2 * min(b))
main()
