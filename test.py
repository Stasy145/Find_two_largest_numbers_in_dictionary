import time

# Algoruthm 1

start_time_1 = time.time()
dict = {'a': 70, 'b': 34, 'c': 900, 'd': 152}

def find_largest_values_1():

    list_1 = []
    for k,v in dict.items():
        list_1.append(v)
        sorted_list = sorted(list_1)
          
    for k,v in dict.items():
        if v >= sorted_list[-2]:
            print(k)
       
find_largest_values_1()

end_time_1 = time.time()
final_time_1 = end_time_1 - start_time_1

print("---------------------")

# Algorithm 2

start_time_2 = time.time()
dict = {'a': 70, 'b': 34, 'c': 900, 'd': 152}

def find_largest_value_2():  
         
    my_list = sorted(list(dict.values()))
    answer = {k:v for k,v in dict.items() if v >= my_list[-2]}
    return answer.keys()
    
print(find_largest_value_2())

end_time_2 = time.time()
final_time_2 = end_time_2 - start_time_2
print("---------------------")
print(final_time_1)
print(final_time_2)

