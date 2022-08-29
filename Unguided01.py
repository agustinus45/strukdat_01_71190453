while True:
    print('Masukkan Input:')
    perhitungan = input()
    def hitung():
        a = perhitungan.split(' ')
        if '+' in a:
            print(int(a[0])+int(a[2]))
        elif '-' in a:
            print(int(a[0])-int(a[2]))
        elif ':' in a:
            print(int(a[0])/int(a[2]))
        elif 'x' in a:
            print(int(a[0])*int(a[2]))
    hitung()
    if 'Q' in perhitungan:
        break    
    
