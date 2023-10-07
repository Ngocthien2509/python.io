import math

class PhanSo:
    def __init__(self, tu=1, mau=1) -> None:
        self.tu = tu
        self.mau = mau
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    
    def rutGon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu = self.tu // ucln
        self.mau = self.mau // ucln
        return self
        
    def __add__(self, other):
        kq = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo()
        kq.tu = self.tu*other.mau + self.mau*other.tu
        kq.mau = self.mau*other.mau
        return kq.rutGon()
    
    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.mau - self.mau*other.tu
        kq.mau = self.mau*other.mau
        return kq.rutGon()
    
    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        return kq.rutGon()
    
    def __truediv__(self, other):
        pass

    

    def laPSAm(self):
        return self.tu*self.mau < 0

a = PhanSo(2,5)
b = PhanSo(1,2)

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

