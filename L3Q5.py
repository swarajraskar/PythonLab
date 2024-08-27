import numpy as np

numbers=[10,20,50,40,30,50,10,20,60]

mean= np.mean(numbers)
median=np.median(numbers)

mode_dict={}
for num in numbers:
  if num in mode_dict:
    mode_dict[num]+=1
  else:
    mode_dict[num]=1
mode= max(mode_dict,key=mode_dict.get)
print(f"mean={mean}, mode={mode}, median={median}")    