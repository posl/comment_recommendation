def get_series(s1, s2, s3):
    series = ["ABC", "ARC", "AGC", "AHC"]
    for s in [s1, s2, s3]:
        series.remove(s)
    return series[0]
