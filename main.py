data = [
    "apel",
    "mangga",
    "jeruk",
    "melon"
]

cari = input("Cari buah: ")

for item in data:

    if cari.lower() in item.lower():
        print("Ketemu:", item)
