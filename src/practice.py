import random

lunch = random.choice(["된장찌개", "파스타", "피자", "스테이크", "제육볶음", "짜장면"])
dinner = random.choice(["된장찌개", "파스타", "피자", "스테이크", "제육볶음", "짜장면"])

# 반복문
for x in range(3):
  print(x, lunch)

print('-----')

print(lunch)
print(dinner)

print('------')

me = {"name": "기현", "age": 30, "sex": "male"} # 딕셔너리

print(me.get("name"))

me = {"사는곳": "연남동"}

print(me.get("사는곳"))
print(me.get("age"))

me["취미"] = "coding"

print(me)
print(len(me))
del me["사는곳"]
print(len(me))
me.clear()
print(me)

print('-----')

foods = ["된장찌개", "파스타", "피자", "스테이크", "제육볶음", "짜장면"]
print(foods[2])
# print(foods[7]) -> error
print(foods[-1])

foods.append("치킨")
print(foods)
foods.remove("피자")
print(foods)
del foods[0]
print(foods)

print('-----')

for x in range(len(foods)):
  print(foods[x])

inform = {"고향": "광주", "취미": "코딩", "좋아하는 음식": "피자"}
for x, y in inform.items():
  print(x)
  print(y)

print('-----')

# 집합
# set, 여러가지 원소의 묶음, 같은 원소가 존재할 수 없음

foods = ["된장찌개", "피자", "제육볶음", "피자"]
foods_set = set(foods) # 안에들어있는 원소의 순서를 보장하지 않음

print(foods)
print(foods_set)

print('-----')

menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["피자", "치킨", "짜장면"])

# 합집합
menu3 = menu1 | menu2
print(menu3)

# 교집합
menu3 = menu1 & menu2
print(menu3)

# 차집합
menu3 = menu1 - menu2
print(menu3)

print('-----')

# if
food = random.choice(["피자", "치킨", "짜장면"])

print(food)

if(food == "짜장면"):
  print('곱배기 주세요')
else:
  print('그냥 주세요')
print('end')

print('-----')

set_dinner = set(['피자', '치킨', '된장찌개', '짜장면'])
food = '짜장면'
set_dinner = set_dinner - set([food])
print(set_dinner)
