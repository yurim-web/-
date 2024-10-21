# 조건

# num = input("숫자입력")
# num_int = int(num)
# if num_int > 0 :
#     print("양의 정수")
# elif num==0:
#     print("0")
# else:
#     print("음의 정수")
#
# print ("프로그램 종료!")



#유저에게 구매한 물품 총액이 50000원 이상이면 10% 할인된 금액 나타내고
#그게 아니면 원래 구매한 금액을 나타내는 프로그램


# price= input("구매한 물품 총액은 얼마이신가요?")
# price_int = int(price)
#
# if price_int >= 50000:
#     print(f"총 금액 : {price_int* 0.9} 입니다")
# else:
#     print(f"총 금액 {price_int} 입니다")



    #영어점수를 유저에게 물어보고
    #90점 이상 A
    #80점 이상 B
    #70점 이상 C
    #60점 이상 D
    #그 외에는 F

score = int(input("당신의 영어점수는?"))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")+
