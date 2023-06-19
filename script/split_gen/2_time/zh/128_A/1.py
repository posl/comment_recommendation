def make_pie(apples, pieces):
    return (apples * 3 + pieces) // 2
print('请输入苹果的个数和苹果的块数，用空格分开')
apples, pieces = map(int, input().split())
print(make_pie(apples, pieces))
