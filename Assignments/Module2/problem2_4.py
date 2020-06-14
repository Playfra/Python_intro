import random

def problem2_4():
    random.seed(70)
    number_list=[]
    for number in range(0,10):
        number = (random.random()*5)+30
        number_list.append(number)
    print(number_list)