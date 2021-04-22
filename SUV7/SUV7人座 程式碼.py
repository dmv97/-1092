print("請輸入體重過輕,正常,過重")
weight= int(input("(1)過輕(2)正常(3)過重\n"))
kg=float(input("請輸入你的體重\n"))
print("請輸入您的工作量")
print("註:輕度指從事靜態之工作。中度指從事活動較多之工作。重度指重度使用體力之工作。")
work=int(input("(1)輕度(2)中度(3)重度\n"))
if weight==1:
    if work==1:
        need=35*kg
    if work==2:
        need=40*kg
    if work==3:
        need=45*kg
if weight==2:
    if work==1:
        need=30*kg
    if work==2:
        need=35*kg
    if work==3:
        need=40*kg
if weight==3:
    if work==1:
        need=23*kg
    if work==2:
        need=30*kg
    if work==3:
        need=35*kg
print('你一天可攝取的量:',need)

a=1
while a>0:

    
    breakfast=int(input("請輸入早餐的熱量"))
    
    b=need-breakfast
    
    if b<0:
        print("今天熱量攝取過多")
    else:
        print("今天剩",b,"熱量")

        lunch=int(input("請輸入午餐的熱量"))

        c=b-lunch

        if c<0:
            print("今天熱量攝取過多")
        else:

        

            print("今天剩",c,"熱量")

            dinner=int(input("請輸入晚餐的熱量"))

            d=c-dinner

            if d<0:
                print("今天熱量攝取過多")
            else:
                
                print("今天剩",d,"熱量")

                
                print("熱量攝取正常")
                


