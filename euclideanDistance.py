import math

# Noktaların tanımlandığı liste
points = [(1, 2), (3, 5), (7, 8), (4, 6), (9, 1)]

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Tüm nokta çiftleri arasındaki mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonucun yazdırılması
print("Verilen noktalar arasındaki minimum Öklid mesafesi:", min_distance)
