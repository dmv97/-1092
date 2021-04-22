# Programming 101
# week 05
# demo 01

#選擇結構1
a=5; b=10
if a>b:
      print("變數a的值比變數b的值大")
      print("a=%4d"%(a))
      print("b=%4d"%(b))
else:
      print("變數a的值沒有比變數b的值大")
      print(f"a={a:10.4f}")
      print(f"b={b:10.4f}")


#選擇結構2      
years= input("請輸入一個西元年：")
year=int(years)
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0)     

if isLeapYear:
      print ("西元",year,"年是閏年") 
else:
      print ("西元",year,"年不是閏年")




