def main():
    N = int(input())
    #print(N)
    hex = str(hex(N))
    #print(hex)
    hex = hex[2:]
    #print(hex)
    if len(hex) == 1:
        hex = '0' + hex
    print(hex)
