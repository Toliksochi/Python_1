A = int(input ("Введите шесть цифр билета"))
S = A // 1000
M = A % 1000
V = S//100 + S//10 % 10 + S % 10
Z = M//100 + M//10 % 10 + M % 10
if V ==Z:
    print ("yes")
else:
    print ("no")
