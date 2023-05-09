def main():
    A, B, C, D, E = map(int, input().split())
    print((A+B+C+D+E-1)//5+9)
