# Programming 101
# week 05
# demo 02

#重複結構1
a=1 #哨兵的初始值
print("印出1~100的正整數:")
while a<=100:   #當哨兵的值>100時，重複結構結束
      print(a)
      #print(a, end=' ')
      a+=1

print()



#重複結構2
year=1
while year > 0:
      years= input("請輸入一個西元年（輸入0代表結束程式）：")
      year=int(years)
      isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0)     
      if year > 0:
            if isLeapYear:
                  print ("西元",year,"年是閏年") 
            else:
                  print ("西元",year,"年不是閏年")


