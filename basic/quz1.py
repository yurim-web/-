#몇년생인지 물어보고, 2005년 이하이면 성인입니다! 아니면 미성년자입니다!

a= input("몇년생이신가요?")
a2="성인입니다" if 2005 >= int(a) else "미성년자입니다"
print(a2)
