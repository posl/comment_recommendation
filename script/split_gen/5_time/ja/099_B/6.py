def main():
    a, b = map(int, input().split())
    print(int((b-a)*(b-a+1)/2 - b))
