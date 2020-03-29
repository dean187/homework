email = 'spartacodingclub@gmail.com'

#채워야하는 함수
def check_mail(email):
    if email.find('@') == -1:
        return False
    else:
        return True

#결과값
print(check_mail(email))

#아래와 같이 출력됩니다
True

email = 'spartacodingclub@gmail.com'

#채워야하는 함수
def get_mail(s):
	## 여기에 코딩을 해주세요
    return s.split('@')[1].split('.')[0]

#결과값
print(get_mail(email)) # gmail

#아래와 같이 출력됩니다
# gmail

#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

temp_dict = {'name': 'bob'}
temp_dict['age'] = 18
print(temp_dict)

#채워야하는 함수
def count_list(a_list):
    result = {}
    for fruit in a_list:
        print(fruit)
        if fruit in result:
            result[fruit] = result[fruit] + 1
        else:
            result[fruit] = 1
        print(result)


    return result

#결과값
print(count_list(a))

#아래와 같이 출력됩니다
#{'사과': 1, '감': 3, '배': 1, '포도': 3, '딸기': 2, '수박': 1}


temp_dict = {'name': 'bob'}
print('age' in temp_dict)


temp_dict['age'] = 18
print('age' in temp_dict)

#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']


#채워야하는 함수
def count_list(a_list):
    result = {}
    for fruit in a_list:
        print("*"*60)
        print("지금 과일: ", fruit)
        print("if 전 result: ", result)
        print("과일 ", fruit, "가 result 안에 있을까? ", fruit in result)
        if fruit in result:
            result[fruit] = result[fruit] + 1
        else:
            result[fruit] = 1
        print("if 후 result: ", result)


    return result

#결과값
print(count_list(a))

# #아래와 같이 출력됩니다
# #{'사과': 1, '감': 3, '배': 1, '포도': 3, '딸기': 2, '수박': 1}
