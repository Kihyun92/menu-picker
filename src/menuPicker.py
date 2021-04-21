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

me = {"name": "기현", "age": 30, "sex": "male"}

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