def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.reverse()
    print(*s, sep='\n')
