# bytes jest używane do przechowywania danych binarnych, takich jak obrazy, itp.
# po prostu to sekwencja bajtów (liczb od 0 do 255)
print(b"\x48\x65\x6C\x6C\x6F")  # b'Hello'

with open("hello.bin", "wb") as file:
    file.write(b"\x48\x65\x6C\x6C\x6F")  # zapisuje się Hello do pliku hello.bin


# str jest używane do przechowywania sekwencji symboli
a = "Hello"
print(a)  # Hello
with open("hello.txt", "w") as file:
    file.write(a)  # zapisuje się Hello do pliku hello.txt


# Kodowanie symboli - sposób reprezentacji symboli na bajty
