!pip install hangul-utils
from hangul_utils import split_syllables, join_jamos

String=[input() for x in range(2)]
String_split=[String[i][j] for i in range(len(String)) for j in range(len(String[i]))]

String_sort=[]
for k in range(len(String_split)-3):
  String_sort.append(String_split[k])
  String_sort.append(String_split[k+3])

jamo=[split_syllables(x) for x in String_sort]

hangeul={
    'ㄱ':2, 'ㄴ':2, 'ㄷ':3, 'ㄹ':5, 'ㅁ':4, 'ㅂ':4, 'ㅅ':2, 'ㅇ':1, 'ㅈ':3, 'ㅊ':4, 'ㅋ':3, 'ㅌ':4, 'ㅍ':4, 'ㅎ':3,
 'ㅏ':2, 'ㅑ':3, 'ㅓ':2, 'ㅕ':3, 'ㅗ':2, 'ㅛ':3, 'ㅜ':2, 'ㅠ':3, 'ㅡ':1, 'ㅣ':1
 }

hangeul_num=[];
for i in jamo:
  for j in i:
    if j in hangeul:
      hangeul_num.append(hangeul[j])
jamo_num=[len(x) for x in jamo]
place=[]; Sum=[]
for y in jamo_num:
  place.append(hangeul_num[0:y])
  del hangeul_num[0:y]


Sum1=[sum(x) for x in place]

a1=[Sum1[x] for x in range(len(Sum1)-1)]; b1=[Sum1[x] for x in range(1,len(Sum1))]
Sum2_n=[a1[x]+b1[x] for x in range(len(a1))]
Sum2=[Sum2_n[x]%10 for x in range(len(Sum2_n))]

a2=[Sum2[x] for x in range(len(Sum2)-1)]; b2=[Sum2[x] for x in range(1,len(Sum2))]
Sum3_n=[a2[x]+b2[x] for x in range(len(a2))]
Sum3=[Sum3_n[x]%10 for x in range(len(Sum3_n))]

a3=[Sum3[x] for x in range(len(Sum3)-1)]; b3=[Sum3[x] for x in range(1,len(Sum3))]
Sum4_n=[a3[x]+b3[x] for x in range(len(a3))]
Sum4=[Sum4_n[x]%10 for x in range(len(Sum4_n))]

a4=[Sum4[x] for x in range(len(Sum4)-1)]; b4=[Sum4[x] for x in range(1,len(Sum4))]
Sum5_n=[a4[x]+b4[x] for x in range(len(a4))]
Sum5=[Sum5_n[x]%10 for x in range(len(Sum5_n))]

if Sum5[0]+Sum5[1] == 0:
  print("{0} ❤️ {1}".format(String[0],String[1]),': 100 %')
else:
  print("{0} ❤️ {1}".format(String[0],String[1]),':',Sum5[0]*10+Sum5[1],'%')
