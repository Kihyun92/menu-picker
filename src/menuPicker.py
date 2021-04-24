import time
import random

dinner = ['피자', '치킨', '짜장면', '햄버거', '제육볶음']

while True:
  print(dinner)
  newItem = input('추가하실 메뉴를 입력해주세요 : ')

  if(newItem == 'q'):
    break
  else:
    dinner.append(newItem)
  
print(dinner)

set_dinner = set(dinner)  # 집합 형태로 변경

while True:
  print(set_dinner)
  item = input('음식을 삭제해주세요: ')

  if(item == 'q'):
    break
  else:
    set_dinner = set_dinner - set([item])

print(set_dinner, '중에서 선택합니다.')

count = 5
while count != 0:
  print(count)
  time.sleep(1)
  count = count -1

print(random.choice(list(set_dinner)))
