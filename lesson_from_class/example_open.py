with open("hello.txt", "a") as example_file:  # 'w' - перезаписывает файл, 'а' - дозаписывает в конце файла
    example_file.write("Hello World\n")
example_file.close()