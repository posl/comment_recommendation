def main():
    a,b = map(int, input().split())
    print(sum(range(1,b-a))-b)
