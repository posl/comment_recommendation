def main():
    n = int(input())
    a = input().split()
    b = input().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    c = [i for i in a if i in b]
    print(len(c))
    d = [i for i in a if i not in b]
    e = [i for i in b if i not in a]
    print(len(d)+len(e))
