# 2024/6/30 11:19
# 素数.py

for i in range(1,10):
    for j in range(2,i):
       if j % i == 0:
           break
       else:
        print(i)

