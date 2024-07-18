def is_prime(num,list):
    #判断素数并收集到list
    if num==0 or num==1:
        return()
    for factor in range(2,num):
        if num%factor==0:
            return()
    list.append(num)
    return()



def delta_lists(n,list1,list2,delta_list):
    #两个列表中数据逐项做差，并收集到delta_list
    for factor in range(n):
        m=list1[factor]-list2[factor]
        delta_list.append(m)
    return()



def extreme_value(max,min,x):
    #极值
    if x >= max:
        max=x
    if x <= min:
        min=x
    return(max,min)



def divide_xy_ans(n,delta_list):
    #区分x,y方向位移并计算
    x,y,xmax,xmin,ymax,ymin=0,0,0,0,0,0
    for factor in range(n):
        if factor%4==0:
            x+=delta_list[factor]
            xmax,xmin=extreme_value(xmax,xmin,x)
            continue
        elif factor%4==1:
            y-=delta_list[factor]
            ymax,ymin=extreme_value(ymax,ymin,y)
            continue
        elif factor%4==2:
            x-=delta_list[factor]
            xmax,xmin=extreme_value(xmax,xmin,x)
            continue
        elif factor%4==3:
            y+=delta_list[factor]
            ymax,ymin=extreme_value(ymax,ymin,y)
    xans=xmax-xmin
    yans=ymax-ymin
    return(xans,yans)



#主体部分
print('问题:在一平面直角坐标系上小云兮在遛狗狗,一开始的运动方向为x轴正方向。\
现记其走过的路程为s,当s为素数时,遛狗的前进方向顺时针旋转90度。\
现问当总路程x等于某一输入值时,其在x轴或y轴方向上所达到的最遥远两端的距离。')
list1=[]
delta_list=[]
num=int(input("请输入移动总路程："))
if num==0 or num==1 or num==2:
    xans=num
    yans=0
else:
    for factor in range(num):
        is_prime(factor,list1)
    list2=list1.copy()
    list2.insert(0,0)
    n=len(list1)
    delta_lists(n,list1,list2,delta_list)
    if num not in list1:
        delta_list.append(num-list1[n-1])
    n_final=len(delta_list)
    xans,yans=divide_xy_ans(n_final,delta_list)
    ans=max(xans,yans) 
print('水平方向的极差=',xans,'竖直方向的极差=',yans,'最大的极差=',ans)