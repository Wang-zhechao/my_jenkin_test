
# If you need to import additional packages or classes, please import here.

def func():

    # please define the python3 input here. For example: a,b = map(int, input().strip().split())
    # please finish the function body here.
    # please define the python3 output here. For example: print().
    input_str = "aaaacc"
    input_str_list = list(input_str)
    output_list = []
    if len(input_str_list) == 1:
        print(1)
    else:
        ord_num = 0
        doub_num = 0
        str_list = []
        for i in set(input_str_list):
            num = input_str_list.count(i)
            if num % 2 == 0:
                doub_num += 1
                for _ in range(int(num/2)):
                    str_list.append(i)
            else:
                ord_num += 1

        if ord_num > 1:
            print(0)
        else:
            for i in range(len(str_list)):
                for j in range(len(str_list) - 1):
                    str_list[j], str_list[j+1] = str_list[j+1], str_list[j]
                    output_list.append("".join(str_list))
            print(output_list)
            print(len(set(output_list)))


if __name__ == "__main__":
    func()
