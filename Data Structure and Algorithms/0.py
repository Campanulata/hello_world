import time

# 给定a,b,c自然数，满足if的条件，求所有可能的值

'''
start_time = time.time()
for a in range(1,1001):
    for b in range(1,1001):
        for c in range(1,1001):
            if a+b+c==1000 and a**2+b**2==c**2:
                print(a,b,c)
end_time = time.time()
print(end_time-start_time)
'''
start_time = time.time()
for a in range(1,1001):
    for b in range(1,1001):
        c=1000-a-b
        if a**2+b**2==c**2:
                print(a,b,c)
end_time = time.time()
print(end_time-start_time)