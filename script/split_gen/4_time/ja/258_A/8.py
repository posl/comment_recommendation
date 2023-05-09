def main():
    k = int(input())
    k += 21 * 60
    print('{:0>2}:{:0>2}'.format(k//60%24,k%60))
