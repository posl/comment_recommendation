def main():
    n = int(input())
    for i in range(2**15):
        if i & n == i:
            print(i)
