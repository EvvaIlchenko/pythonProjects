#По рядку S побудувати текстовий файл, який містить
#символи цього рядка.
S = str(input("string S:"))
f = open('Sf', 'wt')
f.write(S)

f.close()


