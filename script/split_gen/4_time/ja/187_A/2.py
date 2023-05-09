def main():
    a,b = map(int, input().split())
    print(max(sum([int(i) for i in str(a)]), sum([int(i) for i in str(b)])))
