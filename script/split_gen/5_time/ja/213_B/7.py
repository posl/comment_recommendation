def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sort = sorted(a)
    print(a.index(a_sort[1])+1)
