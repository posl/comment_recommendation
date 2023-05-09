def main():
    n = int(input())
    n_str = str(n)
    s = 0
    for i in range(len(n_str)):
        s += int(n_str[i])
    if n % s == 0:
        print('Yes')
    else:
        print('No')
