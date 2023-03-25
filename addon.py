def custom_filter(some_list):
    sum = 0
    for list_element in some_list:
        if (type(list_element) is int):
            if list_element % 7 == 0:
                sum += list_element
    return sum <= 83

def lambda_test(s):
    return s.count('я') >= 23

if __name__ == '__main__':
    list_1 = [7, 14, 28, 32, 32, 56]
    print(custom_filter(list_1))
    list_2 = [7, 14, 28, 32, 32, '56']
    print(custom_filter(list_2))
    #print(lambda_test('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))
    print(lambda x: x.count('я') >= 23)