def main():
    L = int(input())
    print((L/3)**3 if L % 3 == 0 else ((L-1)/3)**3 if L % 3 == 1 else ((L-2)/3)**3)
