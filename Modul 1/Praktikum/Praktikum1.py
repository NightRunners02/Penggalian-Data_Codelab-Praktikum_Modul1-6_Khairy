import random

def manipulate_list(data_list, nim_last_digit):
    for _ in range(10):
        data_list.append(random.choice([random.randint(1, 100), random.uniform(1.0, 100.0)]))

    print("Setelah menambahkan elemen:", data_list)

    if 0 <= nim_last_digit < len(data_list):
        del data_list[nim_last_digit]

    print("Setelah menghapus elemen indeks NIM:", data_list)

    data_list.reverse()
    print("Setelah membalik urutan:", data_list)

    max_value = max(data_list, key=lambda x: float(x))
    data_list.remove(max_value)

    print("Setelah menghapus elemen terbesar:", data_list)

    data_list.sort(reverse=True, key=lambda x: float(x))
    print("Setelah sorting descending:", data_list)

    return data_list

nim_last_digit = 9
initial_list = []
result = manipulate_list(initial_list, nim_last_digit)
print("\nHasil akhir:", result)
