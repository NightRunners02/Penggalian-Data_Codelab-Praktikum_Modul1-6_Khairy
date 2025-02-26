import pandas as pd

produk_dict = {
    "Produk A": 101,
    "Produk B": 102,
    "Produk C": 103,
    "Produk D": 104,
    "Produk E": 105
}
produk_series = pd.Series(produk_dict)
print("Series Produk:")
print(produk_series)

produk_data = {
    "Nama": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "ID": [201, 202, 203, 204, 205],
    "Harga": [15000000, 200000, 500000, 3000000, 2500000],
    "Stok": [10, 50, 30, 15, 20]
}
df = pd.DataFrame(produk_data)
print("\nDataFrame Produk:")
print(df)

kota_pengiriman = ["Jakarta", "Bandung", "Surabaya", "Medan", "Yogyakarta"]
df["Kota"] = kota_pengiriman
print("\nDataFrame setelah menambahkan kolom Kota:")
print(df)

df_sorted = df.sort_values(by="ID")
print("\nDataFrame setelah sorting berdasarkan Nama:")
print(df_sorted)