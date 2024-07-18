def is_prime(num,list):
    #判断素数并收集到list
    if num==0 or num==1:
        return()
    for factor in range(2,num):
        if num%factor==0:
            return()
    list.append(num)
    return()



def extreme_value(max,min,x):
    #极值
    if x >= max:
        max=x
    if x <= min:
        min=x
    return(max,min)



def divide_xy_ans(list,num):
    #区分x,y方向位移并计算
    directions=[(1, 0), (0, -1), (-1, 0), (0, 1)]
    x,y,xmax,xmin,ymax,ymin,direction_index=0,0,0,0,0,0,0
    for factor in range(1,num+1):
        if factor-1 in list:
            direction_index=(direction_index+1)%4
        x, y = x + directions[direction_index][0], y + directions[direction_index][1]
        if direction_index%4==0 or factor%4==2:
            xmax,xmin=extreme_value(xmax,xmin,x)
        else:
            ymax,ymin=extreme_value(ymax,ymin,y)
    xans=xmax-xmin
    yans=ymax-ymin
    return(xans,yans)



#主体部分
print('问题:在一平面直角坐标系上小云兮在遛狗狗,一开始的运动方向为x轴正方向。\
现记其走过的总路程为x,当x为素数时,遛狗的前进方向顺时针旋转90度。\
现问当x等于某一定值时,其在x轴或y轴方向上所达到的最遥远两端的距离。')
list=[]
num=int(input("请输入爬虫的移动总步数："))
if num==0 or num==1 or num==2:
    ans=xans=num
    yans=0
else:
    for factor in range(num):
        is_prime(factor,list)
    xans,yans=divide_xy_ans(list,num)
    ans=max(xans,yans) 
print('水平方向的极差=',xans,'竖直方向的极差=',yans,'最大的极差=',ans)