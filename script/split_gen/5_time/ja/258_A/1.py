def problems258_a():
    K = int(input())
    hour = K // 60
    minute = K % 60
    print("{:02d}:{:02d}".format(hour+21, minute))
