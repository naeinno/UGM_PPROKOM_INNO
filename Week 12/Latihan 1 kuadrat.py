import math

def hitung_diskriminan(a, b, c):
    #Menghitung diskriminan d
    return (b ** 2) - (4 * a * c)

def hitung_solusi(a, b, d):
    #Menemukan x1 dan x2
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2
