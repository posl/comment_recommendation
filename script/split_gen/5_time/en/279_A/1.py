def main():
    s = input()
    s = s.replace("vv", "v v")
    s = s.replace("ww", "w w")
    s = s.replace("vw", "v w")
    s = s.replace("wv", "w v")
    print(s.count("v") + s.count("w"))
