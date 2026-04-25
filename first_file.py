#First
# import re
# sentence = input('Please enter a sentence').lower()
# clean = re.sub(r"[^a-z0-9]", "", sentence)
# reverse = clean[::-1]   
# if clean == reverse:
#     return True
# return False



#Second
ls = [5,4,5,4,6,4]
d = {}

for i in ls:
    if i in d:
        d[i] +=1
    else:
        d[i]=1
for key,value in d.items():
    if value == 1:
        print(key)
