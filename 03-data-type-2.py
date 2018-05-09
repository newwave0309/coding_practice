목록 list, tuple
사전 dictionary

#list[] 대괄호
print("list")
list_a = [1, 2, 3]
print (list_a)
# print(type([1, 2, 3]))
#index는 0부터 시작합니다.
print(list_a[0])
print(list_a[1])
print(list_a[2])
#slice 마지막 인덱스는 포함하지 않는다
print(list_a[0:2])
#append
list_a.append(4)
print(list_a)
#remove
list_a.remove(2)
print(list_a)
#clear
list_a.clear()
print(list_a)

tuple(1, ) 소괄호/ 최소한 값과 쉼표를 적어줘야 tuple로 인지함
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))
#tuple은 한 번 생성 후 내부 값 변경 불가
tuple_a.append(4)

dict(map) {} 중괄호 사용함
key & value
dict_a ={
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])
#edit value
dict_a["pen"] = "something to write"
print(dict_a)

set set([]) / 중복이 자동으로 제거된다
set_a = set([1, 2, 3, 3, 3, 2])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

집합 - 교집합, 합집합, 차집합, 여집합
중복이 없다
교집합 &
print(set_a & set_b)
#합집합 |
print(set_a | set_b)
#차집합 -
print(set_a - set_b)
