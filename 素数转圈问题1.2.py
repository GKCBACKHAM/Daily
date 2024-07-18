def is_prime(n):
    #判断一个数是否为质数
    if n<2:
        return False
    if n<4:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

def extreme_value(max_val,min_val,x):
    # 更新最大值和最小值
    return max(x,max_val),min(x,min_val)

def divide_xy_ans(n,delta_list):
    # 计算x和y方向的最远距离
    x,y,xmax,xmin,ymax,ymin=0,0,0,0,0,0
    for idx,delta in enumerate(delta_list):
        if idx%4==0:
            x+=delta
        elif idx%4==1:
            y-=delta
        elif idx%4==2:
            x-=delta
        elif idx%4==3:
            y+=delta
        xmax,xmin=extreme_value(xmax,xmin,x)
        ymax,ymin=extreme_value(ymax,ymin,y)
    return (xmax-xmin,ymax-ymin)

# 主体部分
print('问题:在一平面直角坐标系上小云兮在遛狗狗，一开始的运动方向为x轴正方向。现记其走过的\
路程为s，当s为素数时，遛狗的前进方向顺时针旋转90度。现问当总路程x等于某一输入值时，\
其在x轴或y轴方向上所达到的最遥远两端的距离。')
num=int(input("请输入移动总路程："))
if num<3:
    xans=ans=num
    yans=0
else:
    prime_numbers=[i for i in range(num) if is_prime(i)]
    delta_list=[prime_numbers[i]-prime_numbers[i-1] for i in range(1,len(prime_numbers))] 
    if num not in prime_numbers:
        delta_list.append(num-prime_numbers[-1])
    xans,yans=divide_xy_ans(len(delta_list),delta_list)
    ans=max(xans,yans)
print('水平方向的极差=',xans,'竖直方向的极差=',yans,'最大的极差=',ans)