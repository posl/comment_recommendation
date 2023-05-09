def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(len(set(a) & set(b)))
    print(len(set(a) & set(b)) - len(set(a) & set(b) & set(zip(a, b))))
