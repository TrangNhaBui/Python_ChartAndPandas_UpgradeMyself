import pandas as pd 
import matplotlib.pyplot as plt
# from pandas.io.formats.style import jinja2 
import numpy as np 
df= pd.read_csv('Book3.csv')
List_categories=['Nuoc','Khong thuc vat','Da','Mam','Duoc','Dua','Thuc vat khac']
List_type=['Min','Max','Range']
List_composer=[i+" "+j for i in List_categories for j in List_type]

#######################################################

Band=np.arange(1,33,3) # truc X
# TẠi sao k cho giá trị từ 1-11? vì 1 band sẽ gồm 11 cột 
# nên các giá trị phải giản cách nhau ra vs 1 khoảng tính toán cho tiện nhìn

################## Cach 1: Store base on "basic" list #############################
List_Range=[] # include list of range for all categories 

for i in [2*n+n-1 for n in range(1,8)]:
    List_Range.append(df[List_composer[i]].tolist())
    
List_Min=[] # include list of min value for all categories 
for j in range (0,len(List_composer),3):
    List_Min.append(df[List_composer[j]].tolist())
###########################################################
################### Cach 2: Store base on List having set in this ################################
'''
List_Min01=[]
for j in range (0,len(List_composer),3):
    List_Min01.append(
        {
            List_composer[j]:df[List_composer[j]].tolist()
        }
    )
List_Range01=[]
for i in [2*n+n-1 for n in range(1,8)]:
    List_Range01.append(
        {
            List_composer[i]:df[List_composer[i]].tolist()
        }
    )
'''
#################### X or Y distance for per chart###########################
step=[]
for i in range(-3,4):
    a=[x/2+0.2*i for x in Band]
    step.append(a)
color=['darkblue','maroon','darkgreen','lime','olive','m','orangered']
########### Vertical bar stacked chart#################################################
'''
for i in range(len(List_Min)):
    plt.bar(np.array(step[i]),hList_Min[i],width=0.2,color='r')
    plt.bar(np.array(step[i]),hList_Range[i],bottom=List_Min[i],width=0.2,color='royalblue')
    
plt.xticks(step[4], ['Band' + str(i) for i in range(1,12)])
plt.ylim(-1.5,1.5)
plt.show()
'''
############# Horizontal bar stacked chart##########################################
for i in range(len(List_Min)):

    #plt.barh(np.array(step[i]),List_Min[i],height=0.1,color='w')
    plt.barh(np.array(step[i]),List_Range[i],left=List_Min[i],height=0.1,color=color[i])

# b=[1,1,1,1,1,1,1,1,1,1]
# c=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
# plt.barh(a,b,height=0.04,color='k')
# plt.barh(a,c,height=0.04,color='k')
plt.yticks(step[4], ['Sigma VH','GammaVH','Beta VH','Sigma VV','Beta VV','Gamma VV','Band 2','Band 3','Band 4','Band 8','NVDI'])
plt.ylabel('Kênh',fontsize=10)
plt.xlabel('Phổ',fontsize=10)
List_categories01=['Nước','Không thực vật','Dà','Mấm','Đước','Dừa','Thực vật khác']
plt.legend(List_categories01)
########################## Line separated into many areas ##############################
line_space_area=[1.3,2.8,4.3,5.8,7.3,8.8,10.3,11.8,13.3,14.8]   
for k in line_space_area:
    plt.axhline(y=k,color='gray',linestyle='-',linewidth=0.5)
plt.show()
'''
plt.xlim(-1,17)
plt.ylim(-2,2)
'''


