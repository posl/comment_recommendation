def main():
    S = input()
    for i in range(10):
        if i not in map(int, S):
            print(i)
            break
