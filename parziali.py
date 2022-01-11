a = [24.25, 24.30, 24.32, 24.21, 24.10, 24.60]


def err_medio(valori):
    element_number = len(valori)
    summ = sum(valori)
    err_med = round((summ / element_number), 3)
    return str(err_med)


def err_massimo(valori):
    element_sort_up = sorted(valori)
    element_sort_down = sorted(valori, reverse=True)
    low = element_sort_up[0]
    high = element_sort_down[0]
    result = (high - low) / 2
    final = str(round(result, 4))
    return final


def err_relativo(valori):
    element_number = len(valori)
    summ = sum(valori)
    element_sort_up = sorted(valori)
    element_sort_down = sorted(valori, reverse=True)
    low = element_sort_up[0]
    high = element_sort_down[0]
    med = round((summ / element_number), 3)
    mas = (high - low) / 2
    rel = (mas / med)
    final = str(round(rel, 4))
    return final + "%"


print(err_medio(a))
print(err_massimo(a))
print(err_relativo(a))
