def main():
    A, B, X = map(int, input().split())
    max = 0
    for i in range(1,10):
        if A * i + B * len(str(i)) <= X:
            max = i
    print(max)
