chuoi = input("Nhap 2 so nguyen: ")
num = chuoi.split()
dau = int(num[0])
cuoi = int(num[1])
while dau >= cuoi:
    chuoi = input("Nhap lai 2 so nguyen(so cuoi lơn hon so dau): ")
    num = chuoi.split()
    dau = int(num[0])
    cuoi = int(num[1])
for i in range(dau, cuoi+1):
    if i%3 ==0 and i%5 ==0:
        print("fizzbuzz")
        continue
    elif i % 3 ==0:
        print("fizz")
        continue
    elif i % 5 ==0:
        print("buzz")
        continue
    print(i)