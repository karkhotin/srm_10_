import math

a = 2
e = 0.001
k = 1
x_arr = [1.25, 1, 0]
y_arr = [2, 0, 0]


def func_1(x1, x2, a):
    return a*x1**2-x2+x2**2-a


def func_2(x1, x2, a):
    return x1-math.sqrt(x2+a)+1


def func_1_deriv_1(x1, x2):
    return  2*a*x1


def func_1_deriv_2(x2, a):
    return 2*x2-1


def func_2_deriv_1(x1, a):
    return 1


def func_2_deriv_2(x2, a):
    return 1/(2*math.sqrt(x2+a))
print('Метод Ньютона:')

while abs(y_arr[k] - y_arr[k - 1]) > e and abs(x_arr[k] - x_arr[k - 1]) > e:
    detA1 = (func_1(y_arr[k - 1], x_arr[k - 1], a) * func_2_deriv_2(x_arr[k - 1], a)) - (
                func_2(y_arr[k - 1], x_arr[k - 1], a) * func_1_deriv_2(y_arr[k - 1], a))
    detA2 = (func_2(y_arr[k - 1], x_arr[k - 1], a) * func_1_deriv_1(x_arr[k - 1], a)) - (
                func_1(y_arr[k - 1], x_arr[k - 1], a) * func_2_deriv_1(y_arr[k - 1], a))
    detJ = (func_1_deriv_1(x_arr[k - 1], a) * func_2_deriv_2(x_arr[k - 1], a)) - (
                func_1_deriv_2(y_arr[k - 1], a) * func_2_deriv_1(y_arr[k - 1], a))
    y_arr[k] = y_arr[k - 1] - detA1 / detJ
    x_arr[k] = x_arr[k - 1] - detA2 / detJ
    print("x1 = ", y_arr[k])
    x1 = y_arr[k] - e / a
    print("x2 = ", x_arr[k])
    x2 = x_arr[k] - e / a
    if k > 1 and (abs(y_arr[k] - y_arr[k - 1]) > e and abs(x_arr[k] - x_arr[k - 1]) > e):
        break
    k += 1
e = 0.001
i = 1
x_arr = [1.25, 0, x_arr[k]]
y_arr = [2, 0, x_arr[k]]
a = 2

print('Метод Ітерацій:')


def func_1(x1):
    return x1 - a


def func_2(x1, x2):
    return x2 - math.sin(x1) - a


def func_1_deriv_1(x1, x2):
    return 1


try:
    while abs(x_arr[i] - x_arr[i - 1]) > e and abs(y_arr[i] - y_arr[i - 1]) > e:
        x_arr[i] = (func_1(y_arr[i - 1]))
        y_arr[i] = (func_2(x_arr[i - 1], y_arr[i - 1]))
        if i < 1 and (abs(x_arr[i] - x_arr[i - 1]) > e and abs(y_arr[i] - y_arr[i - 1]) > e):
            break
        i += 1
        print("x1 =", x_arr[i])
        print("x2 =", y_arr[i])
except:
    pass

