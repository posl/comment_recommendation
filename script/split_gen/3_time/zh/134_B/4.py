def main():
    n, d = map(int, input().split())
    print(int(n/(2*d+1))+1 if n%(2*d+1) != 0 else int(n/(2*d+1)))
