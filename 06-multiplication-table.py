# #단 수 정수화
# M_a = input("몇 단을 출력하시겠습니까")
# M_b = int(M_a)
#
# #곱하기 결과값
# for num in range(1, 10):
#     M_R = M_b * num
#     print (M_b )


# 1) 사용자로부터 몇 단을 출력할 지 받을 것

dan = int(input ("몇 단을 출력 하시겠습니까?"))

# 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것

for num in range(1, 10):
    print ("{} * {} = {}".format(dan, num, dan * num))
