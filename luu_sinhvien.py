import os
import pickle
from student2 import SinhVien2

#Tao 1 doi tuong thuoc lop sinhvien
sv = SinhVien2('Pham Ba Trung', 1999, 10.0)

#Duong dan ten tap tin
path = '/Users/trung/PycharmProjects/pythonProject'
filename = 'sinhvien1.dat'

#Luu tru
with open(os.path.join(path, filename), 'wb') as f:
    pickle.dump(sv, f)
print('Ket thuc qua trinh luu du lieu')