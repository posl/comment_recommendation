def main():
	# 文字列の入力
	S = input()
	T = input()
	# Sの先頭からTを探す
	if S.find(T) != -1:
		print("Yes")
	else:
		print("No")
