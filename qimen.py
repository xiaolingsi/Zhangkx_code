import os
import random
bamen_1=["休","生","伤","杜","景","死","惊","开"]
bamen_2=list("休死伤杜死开惊生景")
jiuxing_1=list("蓬任冲辅英禽芮柱心")
jiuxing_2=list("蓬芮冲辅禽心柱任英")
bashen=list("符蛇阴合虎武地天")
tiangan_list=["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
dizhi_list=list("子丑寅卯辰巳午未申酉戌亥")
tian=list("戊己庚辛壬癸丁丙乙")
liushijiazi={}
for i in range(1,61):
    liushijiazi[i]=tiangan_list[(i-1)%10]+dizhi_list[(i-1)%12]
xun_num=0
while True:
    shichen= input("当前时辰:")
    if shichen in list(liushijiazi.values()):
        break
    else:
        print("输入有误！重新输入！")
while True:
    yinoryang= input("阴阳遁:")
    if yinoryang in ("阴","阳"):
        break
    else:
        print("输入有误！重新输入！")
while True:
    jvshu= int(input("局数:"))
    if jvshu in range(1,10):
        break
    else:
        print("输入有误！重新输入！")
# shichen = random.choice(list(liushijiazi.values()))
# yinoryang=random.choice(("阴","阳"))
# jvshu=int(random.choice(list(range(1,9))))
for i in liushijiazi.keys():
    if shichen==liushijiazi[i]:
        xun_num_1=i
        break
else:
    print("输入有误!")

gong_di= [""]*9
shigan=""
if list(shichen)[0] == "甲":
    zhi=list(shichen)[1]
    if zhi =="子":
        shigan="戊"
    elif zhi=="戌":
        shigan="己"
    elif zhi=="申":
        shigan="庚"
    elif zhi=="午":
        shigan="辛"
    elif zhi=="辰":
        shigan="壬"
    elif zhi=="寅":
        shigan="癸"
else:
    shigan=list(shichen)[0]

xun_num=((xun_num_1-1)//10)+1
gong_di[xun_num-1]="戊"
if yinoryang=="阳":
    j=0
    for i in range(jvshu-1,jvshu+8,1):
        gong_di[i%9]=tian[j]
        j+=1
elif yinoryang=="阴":
    j = 0
    for i in range(jvshu-1,jvshu-10,-1):
        gong_di[i % 9] = tian[j]
        j += 1
xun_dict={1:"戊",2:"己",3:"庚",4:"辛",5:"壬",6:"癸",7:"癸"}
zhifu=xun_dict[xun_num]
gongdi_2=[""]*8
gongdi_2[0]=gong_di[0]
gongdi_2[1]=gong_di[7]
gongdi_2[2]=gong_di[2]
gongdi_2[3]=gong_di[3]
gongdi_2[4]=gong_di[8]
gongdi_2[5]=gong_di[1]
#gongdi_2[6]=gong_di[4]
gongdi_2[6]=gong_di[6]
gongdi_2[7]=gong_di[5]
zhifu_position=0
for i in range(len(gong_di)):
    if gong_di[i]==zhifu:
        zhifu_position=i
        break
# gong_tian=[""]*9
zhifu_xing=jiuxing_2[(zhifu_position)%9]

di_zhifu=0
if zhifu == gong_di[4]:
    di_zhifu=5
else:
    di_zhifu=gongdi_2.index(zhifu)

di_shigan=0
if shigan == gong_di[4]:
    di_shigan=5
else:
    di_shigan=gongdi_2.index(shigan)


if di_shigan>=di_zhifu:
    houyi=di_shigan-di_zhifu
else:
    houyi=di_shigan-di_zhifu+8
a=gongdi_2.copy()
tian_pan=[""]*8
for i in range(8):
    tian_pan[(i+houyi)%8]=a[i]
gongdi_er=gongdi_2[5]
a=tian_pan.index(gongdi_er)
tian_pan[a]+=gong_di[4]

bashen_copy=bashen.copy()
bashen_zhifu=0
for i in range(8):
    if tian_pan[i]==zhifu:
        bashen_zhifu=i
        break
    elif len(str(tian_pan[i]))==2:
        if (str(tian_pan[i])[1]==zhifu or str(tian_pan[i])[0]==zhifu):
            bashen_zhifu = i
            break
shunni=-1
if yinoryang=="阳":
    shunni=1
for i in range(8):
    bashen_copy[(i+bashen_zhifu)%8]=bashen[i*shunni]

gongdi_xing={}
for i in range(9):
    gongdi_xing[gong_di[i]]=jiuxing_2[i]
tianpanshuangxing_position=0
for i in range(len(tian_pan)):
    if len(str(tian_pan[i]))==2:
        tianpanshuangxing_position=i
gongdi_xing[tian_pan[tianpanshuangxing_position]]="芮禽"

tianpan_xing=[""]*8
for i in range(8):
    tianpan_xing[i]=gongdi_xing[tian_pan[i]]

#八门
menhouyi=(xun_num_1-1)%10*shunni
if menhouyi<0:menhouyi+=9
zhishi_position=zhifu_position
zhishi=bamen_2[zhishi_position]
zhishiluogong=(zhishi_position+menhouyi)%9
gongdui_dict={0:0,1:5,2:2,3:3,4:5,5:7,6:6,7:1,8:4}
menshunpan=gongdui_dict[zhishiluogong]
menpan=[""]*8
for i in range(8):
    menpan[(menshunpan+i)%8]=bamen_1[(bamen_1.index(zhishi)+i)%8]

#门干
gongdui_dict_2={0:0,5:1,2:2,3:3,7:5,6:6,1:7,4:8}
mengan=[""]*9
menpan_copy=gong_di.copy()
for i in range(9):
    mengan[(i+gongdui_dict_2[menshunpan])%9]= menpan_copy[(menpan_copy.index(shigan)+i)%9]
#门干与地盘合并盘
hepan=[""]*9
for i in range(9):
    hepan[i]=mengan[i] +"             "+ gong_di[i]

print("时辰:",shichen,"     阴阳:",yinoryang,"     局数:",jvshu)
# print("阴阳:",yinoryang)
# print("局数:",jvshu)
# print("后移:",houyi)
# print("地盘",gong_di)
# print(gongdi_2)
# print("时干",shigan)
# print("值符干",zhifu)
# print(zhifu_position)
# print("值符星",zhifu_xing)
# print("天盘:",tian_pan)
# print(bashen_zhifu)
# print(bashen_copy)
# print(gongdi_xing)
# print(tianpan_xing)
# print(zhishi)
# print(menhouyi)
# print(menshunpan)#值使落顺宫
# print(xun_num_1)
# print(menpan)
# print("门干",mengan)
# print("地",hepan)
print("-"*93)
print("|"+"%14s"%tianpan_xing[3]+"%14s"%(bashen_copy[3])+"|"+"%14s"%tianpan_xing[4]+"%14s"%(bashen_copy[4])+"|"+"%14s"%tianpan_xing[5]+"%14s"%(bashen_copy[5])+"|")
print("|"+"%14s"%menpan[3]+"%14s"%tian_pan[3]+"|"+"%14s"%menpan[4]+"%14s"%tian_pan[4]+"|"+"%14s"%menpan[5]+"%14s"%tian_pan[5]+"|")
print("|"+"%28s"%hepan[3]+"|"+"%28s"%hepan[8]+"|"+"%28s"%hepan[1]+"|")
print("-"*93)
print("|"+"%14s"%tianpan_xing[2]+"%14s"%(bashen_copy[2])+"|"+"%15s"%"   "+"%15s"%"    "+"|"+"%14s"%tianpan_xing[6]+"%14s"%(bashen_copy[6])+"|")
print("|"+"%14s"%menpan[2]+"%14s"%tian_pan[2]+"|"+"%14s"%" "+"%15s"%" "+"|"+"%15s"%menpan[6]+"%14s"%tian_pan[6]+"|")
print("|"+"%28s"%hepan[2]+"|"+"%28s"%hepan[4]+"|"+"%28s"%hepan[6]+"|")
print("-"*93)
print("|"+"%14s"%tianpan_xing[1]+"%14s"%(bashen_copy[1])+"|"+"%14s"%tianpan_xing[0]+"%14s"%(bashen_copy[0])+"|"+"%14s"%tianpan_xing[7]+"%14s"%(bashen_copy[7])+"|")
print("|"+"%14s"%menpan[1]+"%14s"%tian_pan[1]+"|"+"%14s"%menpan[0]+"%14s"%tian_pan[0]+"|"+"%14s"%menpan[7]+"%14s"%tian_pan[7]+"|")
print("|"+"%28s"%hepan[7]+"|"+"%28s"%hepan[0]+"|"+"%28s"%hepan[5]+"|")
print("-"*93)
os.system('pause')