def main():
    s1 = input()
    s2 = input()
    s3 = input()
    series = ['ABC','ARC','AGC','AHC']
    series.remove(s1)
    series.remove(s2)
    series.remove(s3)
    print(series[0])
