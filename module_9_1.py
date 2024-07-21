# "Введение в функциональное программирование"
def apply_all_func(int_list, *functions):
    results = dict()
    for function in functions:
        results.update({function.__name__: function(int_list)})
        # results.setdefault(function.__name__, function(int_list))
    return results


# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# Вывод на консоль:
# {'max': 20, 'min': 6}
# {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
