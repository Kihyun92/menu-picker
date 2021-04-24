dinner = ['피자', '치킨', '짜장면', '햄버거', '제육볶음']
print(dinner)

while True:
  newItem = input('추가하실 메뉴를 입력해주세요 : ')
  dinner.append(newItem)
  print(dinner)