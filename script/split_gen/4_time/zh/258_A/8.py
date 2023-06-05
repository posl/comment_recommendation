def problems258_a():
    K = int(input())
    h = K // 60
    m = K % 60
    print("{0:02d}:{1:02d}".format(21+h,m))
