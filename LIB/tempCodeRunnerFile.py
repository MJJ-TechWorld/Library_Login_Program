credt_data_path = r"C:\Users\HP\Desktop\training\Python\LIB\credentials.txt"
with open(credt_data_path, "r") as f:
    data_list = f.readlines()
    f.seek(0)
    data_str = f.read()
code_pos = data_str.find("EMP102")
print(data_str.index(code_pos))