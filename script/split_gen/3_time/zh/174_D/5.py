def main():
    N = int(input())
    c = input()
    c_list = list(c)
    count = 0
    for i in range(N):
        if c_list[i] == 'W':
            count += 1
    print(count)
