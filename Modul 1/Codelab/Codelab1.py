import random

data_tuples = [
    (random.randint(1, 100), random.uniform(1.0, 100.0), f"str{i}", random.randint(1, 100))
    for i in range(12)
]
print("Data Tuple:", data_tuples)

data_list = [item for tup in data_tuples for item in tup]
print("\nData List:", data_list)

data_list.insert(9, "new_data_1")
data_list.insert(10, "new_data_2")
print("\nSetelah Menambahkan Data Baru:", data_list)

data_list = [item for item in data_list if not isinstance(item, float)]
print("\nSetelah Menghapus Float:", data_list)

data_list.sort(reverse=True, key=lambda x: (isinstance(x, str), x))
print("\nSetelah Sorting Descending:", data_list)
