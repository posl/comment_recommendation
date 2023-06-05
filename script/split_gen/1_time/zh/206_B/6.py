def main():
    n = int(input())
    x = 0
    while True:
        x += 1
        if x*(x+1)/2 >= n:
            break
    print(x)
