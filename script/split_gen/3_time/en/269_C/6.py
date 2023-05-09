def main():
    N = int(input())
    for i in range(2**15):
        if N & i == i:
            print(i)
