# total_dictionary = {}

# while True:
#   question = input('질문: ')

#   if(question == 'q'):
#     break
#   else:
#     total_dictionary[question] = ''


# for i in total_dictionary:
#   print(i)
#   answer = input('답변: ')
#   total_dictionary[i] = answer

# print(total_dictionary)


total_list = []

while True:
  question = input('question: ')

  if (question == 'q'):
    break
  else:
    total_list.append({"question": question, "answer": ''})

for i in total_list:
  print(i['question'])
  answer = input("answer : ")
  i['answer'] = answer

print(total_list)