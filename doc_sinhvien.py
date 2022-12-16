from student2 import SinhVien2
import pickle
import os


#Duong dan ten tap tin
path = '/Users/trung/PycharmProjects/pythonProject'
filename = 'sinhvien1.dat'

#Luu tru
with open(os.path.join(path, filename), 'rb') as f:
    sv = pickle.load(f)
print(type(sv))
print(sv)
print('Ket thuc qua trinh luu du lieu')
