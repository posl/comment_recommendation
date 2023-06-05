def main():
    n = int(input())
    p = input().split()
    q = input().split()
    print(abs(p.index(q)+1-q.index(q)-1))
