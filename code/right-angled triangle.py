# -*-coding: utf-8 -*-
'''
c为一条直角边长，
输入一个值，限定a, b边的长度
只要满足条件，就输出
'''


n = int(input("请输入一个正整数："))
c = 47
for a in range(1, n+1):
	for b in range(1, n+1):
		if a + c > b or a + b >c:
			if a**2 + b**2 == c**2 or a**2+c**2 == b**2:
				print(a, b, c)
