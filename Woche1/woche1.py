# 0.1 Aufgabe 1
# Aktivieren Sie Ihre virtuelle Umgebung und installieren Sie darin das Paket pandas.

# source so_se_19/bin/activate
# pip install --upgrade pip
# pip install pandas

# 0.2 Aufgabe 2
# Definieren Sie drei Variablen von jeweils unterschiedlichem Typ und
# wandeln Sie den Typ um (falls möglich).

x = None
y = 2.0
z = True

print(str(x))               # None
print(int(x))               # TypeError: int() argument must be a string,
                            # a bytes-like object or a number, not 'NoneType'
print(int(y))               # 2
print(str(z))               #True

# 0.3 Aufgabe 3
# Welche der folgenden Anweisungen in der Python-Shell sind richtig und welche nicht?
# Erklären Sie im Falle der inkorrekten Anweisungen, worin das Problem besteht.

t = (4, 7, 9)               # Variable t als Tupel mit den Werten 4, 7 & 9 definiert
s = "Die Sonne scheint"     # Variable s als String definiert
l = [34, 22.1,"777",[3, 4]] # Variable l als Liste definiert
t2 = (4, 8, [45, 91])       # Variable t2 als Tupel definiert
t[0]                        # 4
t[3]                        # Index gibt es nicht, IndexError: tuple index out of range
t(3)                        # kann nicht aufgerufen werden,
                            # TypeError: 'tuple' object is not callable
s[4]                        # 'S'
s[4] = "x"                  # einzelne Werte im String können nicht geändert werden
                            # TypeError: 'str' object does not support item assignment
l[2][0] = "g"               # einzelne Werte im String können nicht geändert werden
                            # TypeError: 'str' object does not support item assignment
l[3][0] = "h"               # 3 auf h geändert
l                           # [34, 22.1, '777', ['h', 4]]
t2[2][0] = 23               # 45 auf 23 geändert

# 0.4 Aufgabe 4
# Mit Hilfe der Funktion len können Sie die Länge eines sequentiellen Objekts berechnen,
# z.B.:
# >>> s = "hallo"
# >>> len(s)
# 5
# Definieren Sie von jedem der Ihnen bekannten sequentiellen Datentypen
# (String, Liste, Tupel) jeweils eine Variable und berechnen Sie Ihre Länge.
# Wie können Sie die Funktion len verwenden, um das letzte Element einer sequentiellen
# Variable (z.B. einer Liste) auszugeben? Zeigen Sie dies an einer der drei zuvor
# definierten sequentiellen Variablen.

s = "Hello, world!"         # Variable s als String definiert
t = (7,13, 23, 42)          # Variable t als Tupel definiert
l = ["ja", "nein", "vielleicht", 0, (7, 13, 23, 42)]    # Variable l als Liste definiert

len(s)                      # 13
len(t)                      # 4
len(l)                      # 5

print(l[len(l)-1])          # (7, 13, 23, 42)

# 0.5 Aufgabe 5
# Welche zwei Sätze verbergen sich hinter dem folgenden Buchstabensalat
# (Hinweis: verwenden Sie den Slicing-Operator):
# “IY otuh ihnakv ei ta ipsr oac endeuwr ef ewaittuhr e1.0 Dpoanr’atm etteelrls ?a nyyooun
# ep riotb awbalsy amni sascecdi dseonmte..”

print(s[:20:2], s[21:55:2], s[56:104:2], s[105::2])
# I think it is a new feature. Don’t tell anyone it was an accident.

print(s[1:20:2], s[22:55:2], s[57:104:2], s[106::2])
# You have a procedure with 10 parameters? you probably missed some.
