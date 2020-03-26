# No 1
class MhsTIF(object):
    def __init__(self, nama, NIM, kotaTinggal, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kotaTinggal
        self.uangSaku = us
        
def cekUrut(nim):
    for nimMhs in range(len(nim)-1,0,-1):
        for i in range(nimMhs):
            if nim[i] > nim[i+1]:
                el = nim[i]
                nim[i] = nim[i+1]
                nim[i+1] = el

a0 = MhsTIF('Bintang', 193, 'Purwodadi', 240000)
a1 = MhsTIF('Ainin', 195, 'Pati', 230000)
a2 = MhsTIF('Danang', 204, 'Sragen', 250000)
a3 = MhsTIF('Cecyl', 210, 'Surakarta', 235000)
a4 = MhsTIF('Alfian', 194, 'Semarang', 240000)
a5 = MhsTIF('Aviza', 187, 'Madiun', 250000)
a6 = MhsTIF('Baity', 211, 'Klaten', 245000)
a7 = MhsTIF('Ulin', 190, 'Madiun', 245000)
a8 = MhsTIF('Viola', 173, 'Boyolali', 245000)
a9 = MhsTIF('Riska', 192, 'Rembang', 270000)
a10 = MhsTIF('Fatwa', 179, 'Boyolali', 230000)
a11 = MhsTIF('Sekar', 188, 'Sulawesi', 300000)

urutan = [a0.NIM, a1.NIM, a2.NIM, a3.NIM, a4.NIM, a5.NIM
          , a6.NIM, a7.NIM, a8.NIM, a9.NIM, a10.NIM, a11.NIM]
cekUrut(urutan)
print(urutan)

# No 2
def Kombinasi(angka):
    for number in range(len(angka)-1,0,-1):
        for i in range(number):
            if angka[i] > angka[i+1]:
                el = angka[i]
                angka[i] = angka[i+1]
                angka[i+1] = el

list1 = [0,2,4,6,8,12,13,15]
Kombinasi(list1)
a = list1

list2 = [1,3,5,7,9,10,11,14]
Kombinasi(list2)
b = list2

list3 = (a+b)
Kombinasi(list3)
c = list3
print(c)

# No 3
from time import time as detak
from random import shuffle as kocok

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        abc = i
        while abc > 0 and nilai < A[abc - 1]:
            A[abc] = A[abc -1]
            abc = abc -1
        A[abc] = nilai

def swap(A, a, b):
    tmp = A[a]
    A[a]= A[b]
    A[b]= tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range (dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

k = []
for i in range(1,6001):
    k.append(i)
kocok(k)

u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak = detak();print('Bubble   : %g detik' %(ak-aw));
aw = detak();selectionSort(u_sel);ak = detak();print('Selection : %g detik' %(ak-aw));
aw = detak();insertionSort(u_ins);ak = detak();print('Insertion : %g detik' %(ak-aw));

