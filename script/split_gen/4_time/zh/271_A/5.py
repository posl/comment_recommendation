def convert_to_hexadecimal(N):
    #将十进制转换为十六进制
    hexadecimal = hex(N)
    #将十六进制转换为大写
    hexadecimal = hexadecimal.upper()
    #去除前缀0X
    hexadecimal = hexadecimal[2:]
    #如果是一位数，则在前面加0
    if len(hexadecimal) == 1:
        hexadecimal = "0" + hexadecimal
    return hexadecimal
N = int(input())
print(convert_to_hexadecimal(N))
