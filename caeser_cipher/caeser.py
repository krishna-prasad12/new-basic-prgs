import string
alphabet = list(string.ascii_lowercase)
new_alpha=list(string.ascii_lowercase)
alphabet=alphabet+new_alpha
print(alphabet)

choice=input('type 1.encode 2.decode of your text\t')
tex=input('input text u want to perform the action on \t').lower()
shift=int(input('input the shift to be used\t'))


def encode_text(tex,shift,choice):
    cipher_text = ''
    if choice=='encode':
        shift*=-1
    elif choice=='decode':
        shift*=1
    for letter in tex:
        leter_pos=tex.index(letter)
        pos=alphabet.index(letter)
        shifts=pos+shift
        new_letter=alphabet[shifts]
        cipher_text+=new_letter
    print( f"encoded text is :{cipher_text}")
encode_text(tex,shift,choice)

# def encode_text(tex,shift,choice):
#     cipher_text = ''
#     if choice=='encode':
#         for letter in tex:
#             leter_pos=tex.index(letter)
#             pos=alphabet.index(letter)
#             shifts=pos+shift
#             new_letter=alphabet[shifts]
#             cipher_text+=new_letter
#         print( f"encoded text is :{cipher_text}")
#     elif choice=='decode':
#         for letter in tex:
#             pos=alphabet.index(letter)
#             shifts = pos - shift
#             new_letter=alphabet[shifts]
#             cipher_text+=new_letter
#         print(f"encoded text is :{cipher_text}")
# encode_text(tex,shift,choice)

# if choice=='encode':
#    cipher= encode_text(tex=tex,shift=shift,choice)
#    print(cipher)
# elif choice=='decode':
#     cipher=decode_text(tex,shift)
#     print(cipher)








