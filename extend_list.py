"""
What output does this produce?
Why?
How would you change it to a more intuitive behavior?
"""


def extend_list(val, input_list=[]):
    input_list.append(val)
    return input_list


def main():
    list1 = extend_list(10)
    list2 = extend_list(123, [])
    list3 = extend_list('a')

    print(f"list1: {list1}")
    print(f"list2: {list2}")
    print(f"list3: {list3}")


if __name__ == "__main__":
    main()
