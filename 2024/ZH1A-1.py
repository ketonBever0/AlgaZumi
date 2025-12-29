# -*- coding: utf-8 -*-
"""ZH1_A_csoport 2024.ipynb

## ZH1 A csoport

##1. Feladat:

Ételszállítási útvonal optimalizálás (Dinamikus programozás)

Egy ételszállító vállalatnak el kell juttatnia ételeket egy hálózat különböző állomásaira. Minden állomás között különböző időt vesz igénybe az út. A cél az, hogy megtaláljuk a legrövidebb időt a kezdő állomásból az összes többi állomás elérésére.

Használj dinamikus programozást, hogy megoldást találj erre a problémára.

Feladat kód:
"""

import sys

def shortest_path_delivery(time_matrix, n):
  # DP táblázat inicializálása
  dp = 
  dp[0] = 

# Két ciklus: az állomások és az utak átvizsgálása
  for i in range(n):
  for j in range(n):
  # Ha van út az i. és j. állomás között
  if .......:
  # Frissítjük a dp[j] értékét, ha az új út gyorsabb
  dp[j] = .......

  # Visszatérünk a legrövidebb időket tartalmazó listával
  return dp

# Példa használat:
time_matrix = [
[ 0, 10, 15, 0], # 0. állomás: 10 és 15 egységnyi idő a 1. és 2. állomásra
[10, 0, 35, 25], # 1. állomás: 10 az 0-ra, 35 a 2-re, 25 a 3-ra
[15, 35, 0, 30], # 2. állomás: 15 az 0-ra, 35 az 1-re, 30 a 3-ra
[ 0, 25, 30, 0] # 3. állomás: 25 az 1-re, 30 a 2-re
]
n = 4
# Kiírjuk a legrövidebb időket az 0. állomástól a többi állomásig
print(shortest_path_delivery(time_matrix, n)) # Várható eredmény: [0, 10, 15, 35]

"""###2. Feladat:

Erőforrás-allokációs probléma (Mohó algoritmus)

Egy vállalatnál különböző erőforrásokat (pl. szerverek) kell kiosztani különböző feladatokhoz. Minden feladatnak van egy időigénye, és minden erőforrásnak van egy rendelkezésre állási ideje. A cél, hogy minél több feladatot tudjunk elvégezni úgy, hogy az erőforrások megfelelően ki vannak osztva.

Feladat kód:
"""

def allocate_resources(task_times, resource_times):
  # Mohó algoritmus az erőforrások kiosztására
  # A feladatok és erőforrások időtartamának növekvő sorrendbe állítása


  task_count = 0 # Kiosztott feladatok számának inicializálása
  i, j = 0, 0 # Indexek inicializálása a feladatok és erőforrások listájához

  # Ciklus, amíg van még feladat vagy erőforrás
  while .............. :
    # Ha a jelenlegi feladat időtartama kisebb vagy egyenlő az aktuális erőforrás időtartamával
    if task_times[i] <= resource_times[j]:
    ........ # Növeljük a kiosztott feladatok számát
    i += 1 # Tovább lépünk a következő feladatra
    j += 1 # Tovább lépünk a következő erőforrásra

    # Visszatérünk a kiosztott feladatok számával
    return task_count

# Példa használat:
task_times = [2, 3, 5, 8, 1] # A feladatok időtartamai
resource_times = [3, 5, 7] # Az erőforrások időtartamai
# Kiírjuk, hány feladatot tudunk kiosztani a rendelkezésre álló erőforrások alapján
print(allocate_resources(task_times, resource_times)) # Várható eredmény: 3

"""### 3. Feladat:

Üzleti befektetési döntések optimalizálása (Dinamikus programozás)

Egy vállalkozás több befektetési lehetőség közül választhat. Minden befektetésnek van egy költsége és várható hozama. A cél, hogy a rendelkezésre álló összegből a maximális hozamot érjük el, anélkül, hogy túllépnénk a költségkeretet.

Feladat kód:
"""

def max_investment_value(values, costs, budget):
  # A befektetések számának meghatározása
  n = len(values)
  # DP táblázat inicializálása
  # dp[i][w] a maximális értéket tárolja i. befektetés figyelembevételével
  # w költségkeret mellett
  dp = ...............

  # Iterálunk az összes befektetésen
  for i in range(1, n + 1):
  # Iterálunk a költségkereteken
  for w in range(budget + 1):
  # Ha az i. befektetés költsége belefér a költségkeretbe
  if costs[i - 1] <= w:
  # A maximális érték a következő két lehetőség közül a nagyobb:
  # 1. Nem vesszük figyelembe az i. befektetést (dp[i - 1][w])
  # 2. Figyelembe vesszük az i. befektetést (values[i - 1] + dp[i - 1][w - costs[i - 1]])
  dp[i][w] = ................
  else:
  # Ha a költség nem fér bele, akkor az előző befektetés maximális értékét vesszük
  dp[i][w] = ..............

  # Visszatérünk a maximális értékkel, amely elérhető a teljes költségkerettel
  return dp[n][budget]

# Példa használat:
values = [60, 100, 120, 80] # A befektetések értékei
costs = [10, 20, 30, 15] # A befektetések költségei
budget = 50 # A rendelkezésre álló költségkeret
# Kiírjuk a maximális befektetési értéket a megadott költségkeret mellett
print(max_investment_value(values, costs, budget)) # Várható eredmény: 220

"""### 4. Feladat: Idő komplexitás

Szemléltest a 3. feladat időkomplexitását különböző méretű adatokon.

### 5. MENTŐ Feladat:

Ha nehézségek merülnek fel az 1. vagy 2. feladattal, lehetőséged van kicserélni őket erre a feladatra. Amennyiben mindhárom feladatot (1, 2 és 4) megoldod, a két legmagasabb pontszám fog figyelembe kerülni az osztályzatodban.

Pénzügyi portfólió kiegyensúlyozása (Mohó algoritmus)

Egy befektetési cégnek különböző eszközöket kell kiegyensúlyoznia egy pénzügyi portfólióban. Az egyes eszközök hozama és kockázata ismert. A cél, hogy a portfólió összesített kockázatát minimalizáljuk, miközben a hozam egy bizonyos szintet elér.

Feladat kód:
"""

def balance_portfolio(returns, risks, target_return):
# Mohó algoritmus, hogy minimalizáljuk a kockázatot adott hozam mellett
# A hozamok és kockázatok arányának kiszámítása és az indexek rendezése
n = len(returns)
items = ................. # Legjobb hozam/kockázat arány alapján rendezve

total_risk = 0 # Összesített kockázat inicializálása
total_return = 0 # Összesített hozam inicializálása
selected_items = [] # Kiválasztott elemek listája

# Iterálunk a rendezett elemek listáján
for i in items:
# Ha az aktuális összesített hozam eléri a célhozamot, kilépünk
if .................. :
break
# Hozzáadjuk az aktuális elemet a kiválasztott elemekhez
selected_items.append(i)
# Frissítjük az összesített kockázatot és hozamot
total_risk += ........
total_return += ............

# Visszatérünk az összesített kockázattal és a kiválasztott elemek indexeivel
return total_risk, selected_items

# Példa használat:
returns = [5, 10, 15, 7, 20] # A hozamok listája
risks = [1, 2, 5, 2, 10] # A kockázatok listája
target_return = 25 # A kívánt célhozam
# Kiírjuk az összesített kockázatot és a kiválasztott elemek indexeit
print(balance_portfolio(returns, risks, target_return)) # Várható eredmény: (3, [0, 3, 1])