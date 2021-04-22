#Programming 101
#week04
#demo1

#字串的比較運算
str1='abcd'
str2='abce'
str3='abc'
print(str1<str2)
print(str1==str2)
print(str1>str2)
print(str1<str3)
a='123'
b=456
#print(a<b) #error

#小組討論
years=input("請輸入一個西元年:") #input()請使用者從鍵盤輸入資料
print(type(years))              #透過intput()收到的資料一律為字串
year=int(years)
print(type(year))
print("(1)你所輸入的年份為西元",year,"年")   
#print("(2)你所輸入的年份為西元"+year+"年")   #error
print("(3)你所輸入的年份為西元"+years+"年")
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0)
print("你所輸入的年份西元",year,"年，是否為閏年?",isLeapYear)


#字串切片運算
greet="Good afternoon!"
print(greet[3])
print(greet[2:5])
print(greet[5:])
print(greet[:10])
print(greet[:])
print(greet[::-1])
print(greet[2:13:2])
print(greet[-3])
#脫逸字元
print("印出一個字串")
print("印出的字串中有\"雙引號\"")
print("印出的字串中有\'單引號\'")
print("印出的字串中有\\倒斜線")
print("印出\n換新行")
print("印出\t Tab")

#字串相關的常見函數
print(len('Maria'))
print(len(greet))
msg='Happy Halloween'
print(msg.find('Hall'))
#print(msg.find('mouse'))
#print(msg.find('hall'))
print(msg.index('Hall'))
#print(msg.index('mouse'))
#print(msg.index('hall'))
msg1='app, apple, pineapple'
print(msg1.count('app'))
print(msg.replace('Halloween','Thanksgiving'))
msg2='Merry Christmas'
print(msg2.startswith('Happy'))

#格式化字串
print("="*50)
name="王曉明"
count=2
score=92.1
#第一種寫法
format_str = "%s，你好。你的第%d次數學考試成績是%f分"
print(format_str % (name, count, score))
print("第%04d次考試"%(count))
print("考試成績是%.4f"%(score))
print("學生姓名是:%10s"%(name))
print("學生姓名是:%-10s"%(name))
print("第%-4d次考試"%(count))
print("="*50)
#第二種寫法
format_str1 = f"{name:s}，你好。你的第{count:d}次數學考試成績是{score:f}分"
print(format_str1)
print(f"第{count:04d}次考試")
print(f"考試成績是{score:.4f}")
print(f"學生姓名是:{name:>10s}")
print("="*50)
#印出的資料有中文時
print("1234567890"*5)
print("%-10s"%("靠左對齊"))
print("%10s"%("靠右對齊"))
print("%-10s%10s"%("靠左對齊","靠右對齊"))
print("1234567890"*5)
print("%-10s"%("left"))
print("%10s"%("right"))
print("%-10s%10s"%("left","right"))
print("1234567890"*5)
str1="靠左對齊"
str2="靠右對齊"
print(f"{str1:<10s}")
print(f"{str2:>10s}")
print(f"{str1:<10s}{str2:>10s}")
      
