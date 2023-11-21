def gregorian_date(jd):
    jd = float(jd) + 2400000.5
    year = 0
    mounth = 0
    day = 0
    hour = 0
    min = 0


    grigo = ''
    z = int(jd)
    f = round(jd % 1, 4)
    if z < 2299161:
        a = z
    else:
        alf = int((z - 1867216.25) / 36524.25)
        a = z + 1 + alf - int(alf / 4)
    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)
    day_time = b - d - int(30.6001 * e) + f
    day = int(day_time)
    if day < 10:
        day_wrt = "0" + str(day)
    else:
        day_wrt = day
    if e < 14:
        mounth = e - 1
    elif e == 14 or e == 15:
        mounth = e - 13
    if mounth > 2:
        year = c - 4716
    elif mounth == 1 or mounth == 2:
        year = c - 4715
    hour = int((day_time - day) * 24)
    min = int((((day_time - day) * 24) - hour) * 60)
    if min < 10:
        min = "0" + str(min)
    grigo = str(day_wrt)+"."+str(mounth)+"."+str(year)+" "+str(hour)+":"+str(min)

    return grigo


def process_data(star_name, filters):
    input_filename = 'astro.dat'
    output_filename = f'{star_name}.txt'
    for i in range(len(filters)):
        filters[i] = filters[i].lower()
    # Чтение данных из файла
    with open(input_filename, 'r') as infile:
        lines = infile.readlines()

    # Находим индексы нужных столбцов в заголовке
    header = lines[0].replace("HJD 24...", "HJD_24...").split()
    name_index = header.index('Object')
    julian_date_index = header.index('HJD_24...')
    filter_index = header.index('Filter')
    magnitude_index = header.index('Magnitude')

    # Фильтруем и обрабатываем данные для заданной звезды
    star_data = []
    for line in lines[1:]:
        data = line.split()
        if len(data) >= max(name_index, julian_date_index, filter_index, magnitude_index) + 1:
            if (data[name_index].lower().replace(" ", "").replace("_", "") == star_name.lower().replace(" ", "").replace("_", "")
                    and filters.__contains__(data[filter_index].lower())):
                star_data.append(data)


    # Сортировка данных по фильтрам и дате
    star_data.sort(key=lambda x: (x[filter_index], float(x[julian_date_index])))

    # Создание нового файла с названием звезды
    with open(output_filename, 'w') as outfile:
        # Запись заголовка
        outfile.write('Julian_date Gregorian_date filter magnitude\n')

        # Заполнение файла отсортированными данными
        for row in star_data:
            greg_date = gregorian_date(row[julian_date_index])
            outfile.write(f'{row[julian_date_index]} {greg_date} {row[filter_index]} {row[magnitude_index]}\n')

    print(f'Файл {output_filename} успешно создан.')


# Пример использования
star_name_input = input('Введите название звезды: ')
filters_input = input('Введите фильтры (разделенные пробелом): ').split()

process_data(star_name_input, filters_input)