'''
 @author: YouYang Wang
 @time: 2021/7/25
 @fatcor: calculate GPA
'''
print('请输入学分、绩点、成绩（用空格分离）输入end结束、输入check查看成绩：')
#-----------------------------------------------------------
def jisuan():
    GPA = 0
    avgGrade = 0
    for i in range( len(credit) ):
        GPA = GPA + credit[i] * gpa[i]
        avgGrade = avgGrade + grade[i] * credit[i]
    #GPA
    GPA = GPA / sum(credit)
    #加权平均分
    avgGrade = avgGrade / sum(credit)
    return GPA , avgGrade
#-----------------------------------------------------------
#初始化三个东西
credit = []
gpa = []
grade = []
while 1:
    down = input()
    if down == 'end':
        break
    elif down == 'check':
        a = jisuan()
        print( '您的加权平均分：' ,a[0],'\n您的GPA是：' , a[1])
    else:
        C,G,GR = map( float , down.split(' ') )
        credit.append(C)
        gpa.append(G)
        grade.append(GR)

