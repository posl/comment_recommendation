def main():
    L = int(input())
    if L%3 != 0:
        print((L/3)**3)
    else:
        print(((L/3)-1)**3)
