from phan_so import PhanSo

class DanhSachPhanSo:
    def __init__(self) -> None:
        self.ds = []

    def xuat(self):
        for ps in self.ds:
            print(ps, end = '\t')
    
    def them(self, ps):
        self.ds.append(ps)
    
    def demPSAm(self):
        kq = 0
        for ps in self.ds:
            if ps.laPSAm():
                kq += 1
        return kq
    
    def timPSDuongMin(self):
        kq = PhanSo(0,1)
        for ps in self.ds:
            if ps.tu*ps.mau < 0:
                kq = ps

        return kq

    
