from downloader import download

url = input("Masukan URL: ")
folder = input("Mau di taruh mana?: ")
format_media = input("Mau jadi apa?: ")

hasil = download(url, folder, format_media)

if hasil:
    print("Berhasil")
else:
    print("Gagal")
