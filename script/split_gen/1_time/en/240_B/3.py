def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a]
    a = set(a)
    print(len(a))
