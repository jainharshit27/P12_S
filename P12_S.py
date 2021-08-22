def list_count(a_list):
    count = 0
    for i in a_list:
        count += 1
        print(count,":",i)
    print("Number of values:", count)


list_count([0,0,0,0,0,0,0,0,0])