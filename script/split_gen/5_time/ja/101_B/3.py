def main():
    n = int(input())
    if n % sum(list(map(int, list(str(n))))) == 0:
        print('Yes')
    else:
        print('No')
