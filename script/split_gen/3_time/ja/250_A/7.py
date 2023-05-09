def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print("h:{}, w:{}, r:{}, c:{}".format(h, w, r, c))
    print("ans:{}".format((h-r+1)*(w-c+1)))
