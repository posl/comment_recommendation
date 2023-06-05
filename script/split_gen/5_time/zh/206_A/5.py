def main():
    # input
    n = int(input())
    # process
    ans = 'Yay!' if int(1.08*n) < 206 else 'so-so' if int(1.08*n) == 206 else ':('
    # output
    print(ans)
