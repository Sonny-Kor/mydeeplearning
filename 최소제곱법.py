import numpy as np

x = [2, 4, 6, 8]
y = [81, 93, 91, 97]

mx = np.mean(x)
my = np.mean(y)

def top (x, mx, y, my):
    d = 0
    for i in range(len(x)):
        for i in range(len(x)):
            d += (x[i]-mx)*(y[i]-my)
        return d

divisor = sum([(i - mx)**2 for i in x]) # 분모
dividend = top(x,mx,y,my)

a = dividend/divisor
b = my- (mx*a)

print("y = " + str(a) +"x + "+str(b))