str=input()
alp=[0]*26
str=str.upper()
for x in str:
    alp[ord(x)-65]+=1
idx=alp.index(max(alp))
if alp.count(max(alp))>1:print('?')
else:print(chr(idx+65))