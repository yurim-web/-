# e,i 인지 물어보기
# s,n 인지 물어보기
# t,f 인지 물어보기
# j,p 인지 물어보기


# a= input("몇년생이신가요?")
# a2="성인입니다" if 2005 >= int(a) else "미성년자입니다"
# print(a2)


a=input("e 인가요 i 인가요?")

ei="외향적이시네요!" if str(a)=="e"  else "내향적이시네요!"


b=input("s인가요 n인가요?")
sn="감각적이시네요!" if str(b)=="s" else "직관적이시네요!"


c=input("t인가요 f인가요?")
tf="이성적이시네요!" if str(c)=="t" else "감성적이시네요!"


d=input("j인가요 p인가요?")
jp="계획적이시군요!" if str(d)=="j"  else "즉흥적이시군요!"


print(f"당신의 성향은 {ei} {sn} {tf} {jp} 이시군요!!!!")