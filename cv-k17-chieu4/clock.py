import cv2 as cv
import numpy as np
import math
import random
from datetime import datetime

# Kích thước ảnh và tâm đồng hồ
size = 600
center = (size // 2, size // 2)
radius = 250

# Tạo nền màu tím
clock = np.zeros((size, size, 3), dtype=np.uint8)
clock[:] = (128, 0, 128)  # BGR: tím

# Vẽ vòng tròn đồng hồ
cv.circle(clock, center, radius, (255, 255, 255), 8)

# Các số La Mã
roman_nums = ["IX",  "XII",  "III",  "VI", ]

# Vẽ số La Mã quanh mặt đồng hồ
for i, num in enumerate(roman_nums):
    angle = math.radians(i * 90 - 180)  
    x = int(center[0] + (radius - 40) * math.cos(angle))
    y = int(center[1] + (radius - 40) * math.sin(angle))
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))  # màu ngẫu nhiên
    cv.putText(clock, num, (x-20, y+10), cv.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv.LINE_AA)


now = datetime.now()
hour = now.hour % 12
minute = now.minute
second = now.second


hour_angle = math.radians((hour + minute/60) * 30 - 90)
minute_angle = math.radians(minute * 6 - 90)
second_angle = math.radians(second * 6 - 90)

# Vẽ kim giờ (xanh dương)
hx = int(center[0] + (radius - 120) * math.cos(hour_angle))
hy = int(center[1] + (radius - 120) * math.sin(hour_angle))
cv.line(clock, center, (hx, hy), (255, 0, 0), 8)

# Vẽ kim phút (xanh lá)
mx = int(center[0] + (radius - 80) * math.cos(minute_angle))
my = int(center[1] + (radius - 80) * math.sin(minute_angle))
cv.line(clock, center, (mx, my), (0, 255, 0), 6)

# Vẽ kim giây (đỏ)
sx = int(center[0] + (radius - 60) * math.cos(second_angle))
sy = int(center[1] + (radius - 60) * math.sin(second_angle))
cv.line(clock, center, (sx, sy), (0, 0, 255), 2)

# Hiển thị đồng hồ
cv.imshow("Clock", clock)
cv.waitKey(0)
cv.destroyAllWindows()