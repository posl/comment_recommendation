def main():
    N = int(input())
    for i in range(2**15):
        if i & N == i:
            print(i)
