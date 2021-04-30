# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

def sumList(list):
    s = 0.0
    n = len(list)
    for i in range(n):
        s += list[i]
    return s

def moy(list):
    return sumList(list) / len(list)

def multpl(l1, l2):
    result = []
    i = 0; j= 0;

    while i < len(l1):
        while j < len(l2):
            result.append(l1[i] * l2[j])
            j +=1; i+=1;
    return result

#calculate a & b
def cov(x,y):
    n = len(y);
    return sum(multpl(x,y)) -n*moy(x)*moy(y);

def var(v):
    return  cov(v,v)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(cov([2,2,2] , [3,5,3]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
