from kuadrat import hitung_diskriminan, hitung_solusi

def main():
    # Input koefisien dari keyboard
    a = int(input('Masukkan a: '))
    b = int(input('Masukkan b: '))
    c = int(input('Masukkan c: '))

    # Hitung diskriminan d
    d = hitung_diskriminan(a, b, c)

    if d < 0:
        print("Persamaan tidak memiliki solusi real.")
    else:
        x1, x2 = hitung_solusi(a, b, d)
        print('Solusinya adalah {0} dan {1}'.format(x1, x2))

if __name__ == "__main__":
    main()
