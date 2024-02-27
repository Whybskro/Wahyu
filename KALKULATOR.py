class kalkulator:
    def plus(self,a,b):
        hasil=a+b
        return print(f"hasil dari{a}+{b} adalah {hasil}")
    def mines(self,a,b):
        hasil=a-b
        return print(f"hasil dari{a}-{b} adalah {hasil}")
    def kali(self,a,b):
        hasil=a*b
        return print(f"hasil dari{a}x{b} adalah {hasil}")
    def bagi(self,a,b):
        if b == '0':
            print("Error!Tidak bisa dibagi 0")
        else :
            hasil = a/b
            return print(f"hasil dari{a}:{b} adalah {hasil}")
def main():
    cal=kalkulator()
    while True :
        print("======== APLIKASI SEDERHANA ========")
        print("1. Kalkulator")
        print("2. Exit")
        s1 = input("MASUKKAN PILIHAN ANDA(1/2): ")
        if s1 == '1' :
            a = int(input("Masukkan Angka Pertama: "))
            b = int(input("Masukkan Angka Kedua: "))
            print("============Metode Operasi============")
            print("1. Penjumlahan")
            print("2. Pengurangan")
            print("3. Perkalian")
            print("4. Pembagian")

            o=input("Masukkan Operasi: ")
            if o=='1':
                cal.plus(a,b)
            elif o=='2':
                cal.mines(a,b)
            elif o=='3':
                cal.kali(a,b)
            elif o=='4':
                cal.bagi(a,b)
            else:
                print('tidak valid')
        elif s1=='2':
            print("Terimakasih")
        else:
            print('tidak valid')
            
            
if __name__ == "__main__":
    main()