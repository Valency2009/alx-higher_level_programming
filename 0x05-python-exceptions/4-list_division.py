#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for count in range(list_length):
        try:
            result = my_list_1[count] / my_list_2[count]
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
