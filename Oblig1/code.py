import scipy.stats as stats
import matplotlib.pyplot as mp
import re
#Oppgave 1

#c)
#P(Y>= 300)
print("Oppgave 1\nc)")
x = 17
n = 24
p = 18/37
ans = 1 - stats.binom.cdf(x,n,p)
print("Vinner minst 300 = " +str(ans))

#P(Y<=-300)
x = 6
ans = stats.binom.cdf(x,n,p)
print("Taper minst 300 = " + str(ans))


#d)
#P(Y>= 300)
print("\nd)")
x = 5
p = 6/38
ans =  1 - stats.binom.cdf(x,n,p)
print("Vinner minst 300 = " + str(ans))
#P(Y<= -300)
x = 2
ans = stats.binom.cdf(x,n,p)
print("Taper minst 300 = " + str(ans))

#e)
print("\ne)\n---plot---")
r = 3
p = 4/37
punktsannsynlighet = []
xaxis = []
for x in range(0,999):
    punktsannsynlighet.append(stats.nbinom.pmf(x/10,r,p))
    xaxis.append(x/10)

mp.plot(xaxis, punktsannsynlighet)
mp.xlabel("Z")
mp.ylabel("Punktsannsynlighet")
mp.grid()
mp.title("Negativ Binomisk Fordeling for Z, gitt r = 3 og p = 4/37")
#mp.show()

# f)
print("\nf)")
x = 15-3
ans = stats.nbinom.cdf(x,r,p)
print("Vinner minst 300: " + str(ans))
x = 39-3
ans =  1 - stats.nbinom.cdf(x,r,p)
print("Taper minst 300: " + str(ans))




#Oppgave 2
print("\nOppgave 2\nc) \n---plot--- ")
# c)
file = open("../SRC/doedelighet.txt", "r")
line = file.readline()
dod = []
#Catch each value of doedelighet.txt
for line in file:
    tmp = re.search(r"\d*\s*(\d*.*)", line).group(1)
    dod.append(float(tmp)*0.001)

#Create S(x), F(x) and finally p(x).
def S(x):
    res = 1
    for i in range(0,x+1):
        res *= (1 - dod[35+i])
    return res


def F(x):
    return 1 - S(x)

def p(x):
    return  F(x) - F(x-1)

punktsannsynlighet = []
xaxis = []

for i in range(0, 71):
    punktsannsynlighet.append(p(i))
    xaxis.append(i)

mp.figure()
mp.plot(xaxis, punktsannsynlighet)
mp.xlabel("x - antall år eldre enn 35år")
mp.ylabel("p(x)")
mp.title("Punktsannsynligheten for at mannen dør om nøyaktig x år. ")
mp.grid()


# f)
print("\nf)")
print("---plot---")
def h(X):
    res = 0
    if(X < 35): return res
    for k in range(35, X):
        res += 100000/ 1.03**k
    return res

#Create E[H(x)] = Sum(h(x)*p(x))
forventet_naaverdi_ut = 0
for x in range(0, 71):
    forventet_naaverdi_ut += h(x) * p(x)

print("Forventet nåverdi av pensjonsutbetalingene er: "  +str(forventet_naaverdi_ut))

# i)
#Create E[g(x)]
print("\ni)")

def g(X):
    res = 0
    limit = min(X, 34)
    for k in range(0,limit):
        res += 1/1.03**k
    return res

forventet_naaverdi_inn = 0
for x in range(0,71):
    forventet_naaverdi_inn += g(x) * p(x)
print("Forventet nåverdi av mannens samlede premieinnbetalinger = K * " +str(forventet_naaverdi_inn))


# j)
print("\nj)")
K = forventet_naaverdi_ut / forventet_naaverdi_inn
print("Mannen må betale en årlig premie på: " + str(K))









#
