import pandas as pd
import statistics

data = {
    "Brand": ["Apple", "Xiaomi", "Samsung", "Infinix", "Oppo", "Asus", "Lenovo", "Huawei", "Google Pixel", "Sony"],
    "Tahun Rilis": [2015, 2017, 2018, 2015, 2017, 2020, 2019, 2019, 2020, 2017],
    "Terjual": [150, 75, 120, 85, 75, 120, 50, 90, 55, 50],
    "Harga (juta)": [19, 9, 10, 9, 4, 9, 15, 15, 15, 11],
    "Jenis Penjualan": ["Online", "Offline", "Online", "Online", "Offline", "Online", "Offline", "Online", "Offline", "Offline"]
}
df = pd.DataFrame(data)

print("Ringkasan Statistik:")
print(df.describe())

df["Penghasilan"] = df["Harga (juta)"] * df["Terjual"]
top_brands = df.nlargest(3, "Penghasilan")
print("\n3 Brand dengan Penghasilan Terbesar:")
print(top_brands[["Brand", "Penghasilan"]])

jenis_penjualan_grouped = df.groupby("Jenis Penjualan")["Brand"].apply(list)
print("\nBrand dengan Jenis Penjualan yang Sama:")
print(jenis_penjualan_grouped)

q1 = df["Harga (juta)"].quantile(0.25)
q3 = df["Harga (juta)"].quantile(0.75)

def kategori_harga(harga):
    if harga < q1:
        return "Murah"
    elif harga > q3:
        return "Mahal"
    else:
        return "Sedang"

df["Kategori"] = df["Harga (juta)"].apply(kategori_harga)
print("\nDataFrame dengan Kategori Harga:")
print(df)
