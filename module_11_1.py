import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# =============================================== Lib Pillow ===========================================================
size = (128, 128)
for infile in os.listdir():
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)  # Указываем размеры файла
                im.save(outfile, "JPEG")  # Сохраняем файл
                print(f'converting "{infile}" to "{outfile}" complited ')
                box = (0, 0, 64, 64)  # Создаём кортеж, указываем стартовую точку и размеры
                region = im.crop(box)  # Получаем вырезанное изображение
                region = region.transpose(Image.Transpose.ROTATE_90)  # Поворачиваем вырезанный участок на 90 градусов
                im.paste(region, box)
                im.save('box.jpg', "JPEG")
                im.show()  # Открываем файл
        except OSError:
            # print("cannot create thumbnail for", infile)
            pass

# =============================================== Lib Matplotlib =======================================================
x = np.linspace(0, 2, 100)  # Данные для разметки графика
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='Первая линия (Y = X)')
ax.plot(x, x ** 2, label='Вторая линия (Y = X^2)')
ax.plot(x, x ** 3, label='Третья линия (Y = X^3)')
ax.set_xlabel('ось X')  # Добавляем название оси X
ax.set_ylabel('ось Y')  # Добавляем название оси Y
ax.set_title("Тестовый график")  # Добавляем название графика
ax.legend()  # Добавляем список обозначений на графике
plt.show()
