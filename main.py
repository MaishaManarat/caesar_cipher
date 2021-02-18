alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art

print(art.logo)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def ceasar(text, shift, direction):
  if shift > len(alphabet):
    shift =shift%25 #in case the shift number is too big



  en_de = []
  m = list(text)
  for i in range(0, len(m)):
    if m[i] not in alphabet:
      blank = m[i]
      en_de.append(blank)
    else:
      x = alphabet.index(m[i])
      if direction == 'encode':
        if x+shift < len(alphabet):
          new = alphabet[x+shift]
          en_de.append(new)
        else:
          new = alphabet[x+shift-len(alphabet)]
          en_de.append(new)
      elif direction == 'decode':
        if x-shift >= 0:
          new = alphabet[x-shift]
          en_de.append(new)
        else:
          new = alphabet[x-shift+len(alphabet)]
          en_de.append(new)


  result= ''
  for element in en_de:
      result += str(element)

  print(result)

  print("Do you want to restart the cipher? enter yes or no")
  restart = input()
  if restart == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)
  else:
    print("Goodbye")



ceasar(text, shift, direction)
