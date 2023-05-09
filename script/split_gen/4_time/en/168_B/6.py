def main():
    # get input
    k = int(input())
    s = input()
    # check length of s
    if len(s) <= k:
        print(s)
    else:
        print(s[0:k] + "...")
