number_first = int(input('Введите число: '))
number_second = int(input('Введите число: '))
number_third = int(input('Введите число: '))
if number_first == number_second and number_first == number_third and number_second == number_third:
    print ('3')
elif number_first == number_second or number_first == number_third or number_second == number_third:
    print('2')
elif number_first != number_second and number_first != number_third and number_second != number_third:
    print ('0')
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
