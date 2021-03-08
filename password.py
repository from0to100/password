# 判斷密碼輸入正確或錯誤
# 密碼輸入錯誤，顯示剩餘幾次
# 錯誤超過三次，鎖住密碼
# 密碼正確，不需繼續輸入

password = 'password123'
i = 3

while i > 0:
	i = i - 1
	x = input('Please enter password')
	if x == password:
		print('登入成功')
		break
	elif x != password:
		if i >= 1:
			print('密碼錯誤，你還有', i, '次機會嘗試密碼')
		if i < 1:
			print('密碼錯誤超過3次，請聯絡客服')