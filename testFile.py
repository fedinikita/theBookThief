import os


# смена директории
# os.replace("books/5 уровней лидерства.html",
#            "books/ЗОЖ/5 уровней лидерства.html")

# сохранение в файл
# with open("categories.txt", "w") as file:
#     for item in directory:
#         file.write("%s\n" % item)

################################################################
# # фасовка по директориям
# directions = ['Саморазвитие', 'ЗОЖ',
#               'Семья', 'Общество', 'Бизнес', 'Деньги', 'Технологии']
# directories = ['selfDevelopment', 'zoj',
#                'family', 'society', 'bussines', 'money', 'technology']
# for i in range(len(directories)):
#     l = []
#     with open(f'new/{directories[i]}.txt') as f:
#         l = f.read().splitlines()
#     for j in range(len(l)):
#         os.replace(f'C:\\Users\\Lord\\Desktop\\TrueBooks\\{l[j]}',
#                    f'C:\\Users\\Lord\\Desktop\\TrueBooks\\{directions[i]}\\{l[j]}')
        # файл в список
        # l = []
        # for i in range(len(directions)):
        # with open(f'categories/all.txt') as f:
        #     l = f.read().splitlines()
        # for j in range(len(l)):
        #     if (j != 385):
        #         shutil.copy(f"C:\\Users\\Lord\\Desktop\\pythonProj\\books\\{l[j]}.pdf",
        #                     f"C:\\Users\\Lord\\Desktop\\TrueBooks\\{l[j]}\\{l[j]}.pdf")

        #######################################################################################################
        # преобразование в pdf

        # l = []
        # with open('count.txt') as f:
        #     count = int(f.read())
        # with open('categories/all.txt') as f:
        #     l = f.read().splitlines()
        # for i in range(count, len(l)):
        #     count += 1  # len(l)
        #     with open('count.txt', "w", encoding='utf-8') as file:
        #         file.write(str(count))
        #     pdfkit.from_file(f'books/{l[i]}.html', f'books/{l[i]}.pdf')
        #     print(f'{l[i]} DONE! {count - 1} по счету!')
        ################################################################

        # убирание тегов img
        # with open('categories/all.txt') as f:
        #     booksTittles = f.read().splitlines()

        # for i in range(len(booksTittles)):
        #     with open(f"C:\\Users\\Lord\\Desktop\\books3\\{booksTittles[i]}.html", "r", encoding='utf-8') as file:
        #         l = file.read()
        #     clean_data = re.sub("(<img.*?>)", "", l, 0, re.IGNORECASE |
        #                         re.DOTALL | re.MULTILINE)
        #     with open(f"C:\\Users\\Lord\\Desktop\\books3\\{booksTittles[i]}.html", "w", encoding='utf-8') as file:
        #         file.write(clean_data)

path = r"C:\Users\conif\Desktop\Prekoldes"
os.mkdir(path)
