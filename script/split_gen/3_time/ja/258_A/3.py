def main():
    k = int(input())
    if k < 60:
        print("21:{}".format(k))
    else:
        print("22:{}".format(k - 60))
