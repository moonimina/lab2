from algorithms import single_linear_s
from algorithms import single_binary_s
from algorithms import merge_sort
from overloadings import Products
import pandas as pd
import time
import timeit
import random
from collections import defaultdict

t_linear = []
t_binary = []
t_binary_merge = []
t_key = []
#t_merge = []

n_ = [100, 500, 1000, 5000, 10000, 50000, 100000]

products = {}
for j in n_:
    d = pd.read_excel('./export1.xlsx', sheet_name=f'n={j}').to_dict('records')
    d_products = []
    for product in d:
        d_products.append(Products(
            product['Наименование'], product['Страна'], product['Oбъем'], product['Сумма']))
    products[j] = d_products

#def toFixed(num, digits=0):
#    return f"{num:.{digits}f}"

for l in n_:
    prod_n = [s.prod_name for s in products[l]]
    key = Products(random.choice(prod_n), "", "", "")
    #key = Products("фнысыътц", "", "", "")
    res_linear = []
    #time_start = time.time()
    time_start = timeit.default_timer()
    p = single_linear_s(products[l], 0, len(products[l])-1, key)
    while p != -1:
        res_linear.append(products[l][p].prod_name)
        p = single_linear_s(products[l], p+1, len(products[l])-1, key)
    #time_end = time.time() - time_start
    time_end = timeit.default_timer() - time_start
    t_linear.append(time_end)
    print("linear", l, res_linear)

    res_key = []
    product_multimap = defaultdict(list)
    for prod in products[l]:
        product_multimap[prod.prod_name].append(prod)
    #time_start = time.time()
    time_start = timeit.default_timer()
    b = product_multimap[key.prod_name]
    for v in range(len(b)):
        res_key.append(b[v].prod_name)
    #time_end = time.time() - time_start
    time_end = timeit.default_timer() - time_start
    print("key", l, res_key)
    t_key.append(time_end)

    res_binary_merge = []
    #time_start = time.time()
    time_start = timeit.default_timer()
    merge_sort(products[l], 0, len(products[l]) - 1)
    m = single_binary_s(products[l], 0, len(products[l]), key)
    if m != -1:
        f = m
        while products[l][f] == key and f >= 0:
            res_binary_merge.append(products[l][f].prod_name)
            f -= 1
        f = m + 1
        while products[l][f] == key and f < len(products[l]):
            res_binary_merge.append(products[l][f].prod_name)
            f += 1
    #time_end = time.time() - time_start
    time_end = timeit.default_timer() - time_start
    t_binary_merge.append(time_end)
    print("binary merge", l, res_binary_merge)

    res_binary = []
    #time_start = time.time()
    time_start = timeit.default_timer()
    m = single_binary_s(products[l], 0, len(products[l]) - 1, key)
    if m != -1:
        k = m
        while products[l][k] == key and k >= 0:
            res_binary.append(products[l][k].prod_name)
            k -= 1
        k = m + 1
        while products[l][k] == key and k < len(products[l]):
            res_binary.append(products[l][k].prod_name)
            k += 1
    #time_end = time.time() - time_start
    time_end = timeit.default_timer() - time_start
    t_binary.append(time_end)
    print("binary", l, res_binary)

print('Простой поиск занял', t_linear, 'секунд')
print('Бинарный поиск занял', t_binary, 'секунд')
print('Сортировка с бинарным поиском заняла', t_binary_merge, 'секунд')
print('Поиск по ключу занял', t_key, 'секунд')
