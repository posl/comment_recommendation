def main():
    n = int(input())
    print(sum([1 for i in range(1, n+1) if len(str(i)) % 2 == 0 and str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]]))
