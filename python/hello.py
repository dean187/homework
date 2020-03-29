a_dict = {}
a_dict = {'name':'bob','age':21}
a_dict['height'] = 178 #리스트는 append를 써야하지만 딕셔너리는 바로 붙여넣을수 있음

print(a_dict)
# a_dict의 값은? {'name':'bob','age':21, 'height':178}
# a_dict['name']의 값은? 'bob'
# a_dict['age']의 값은? 21
# a_dict['height']의 값은? 178

people = [{'name':'bob','age':20},{'name':'carry','age':38}]
print(people)
# people[0]['name']의 값은? 'bob'
# people[1]['name']의 값은? 'carry'

person = {'name':'john','age':7}
people.append(person)

print(people)

# people의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
# people[2]['name']의 값은? 'john'

# for asd in people.....plople안에 내용을 알아서 나눠서 asd에 담아줘 asd이름은 아무거나 상관없음

def sum_all(a,b,c):
	return a+b+c

def mul(a,b):
	return a*b

result = sum_all(1,2,3) + mul(10,10)
print(result)
# result라는 변수의 값은?

def minus(a,b):
	return a-b

result2 = minus(mul(10,10),sum_all(1,2,3))
print(result2)
# result2라는 변수의 값은?

def oddeven(num):  # oddeven이라는 이름의 함수를 정의한다. num을 변수로 받는다.
	if num % 2 == 0: # num을 2로 나눈 나머지가 0이면
		 return True   # True (참)을 반환한다.
	else:            # 아니면,
		 return False  # False (거짓)을 반환한다.

def checkbob(name):
	if name == 'bob': # name이 'bob'이면 True를, 아니면 False를 반환해라
		return True
	else:
		return False

print(oddeven(3))
print(checkbob('bob'))

a_list = [1, 2, 3, 4, 5]
b_list = range(1,6)

for a in b_list:
	print(a)


people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

# 모든 사람의 이름과 나이를 출력해봅시다.
for person in people:
    print(person['name'], person['age'])

