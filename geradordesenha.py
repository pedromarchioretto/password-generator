import random

nums = "123456789"
letts = "abcdefghijklmnopqrstuvwxyz"
sins = "!@#$%&*"
length = ''
_type = ''

def genPass(length, *args):
  chars = ''
  password = ''
  for str in args:
    chars = chars + str #juntando os tipos de caracteres desejados

  _list = list(chars) #colocando em uma lista para fazer o shuffle
  random.shuffle(_list)
  chars = ''.join(_list)


  for x in range(length):
    password += random.choice(chars)

  return print('\n A sua senha é -> \033[32m'+ password + "\033[m\n\n\n")

perm = False
print('+-----------------------------------+')
print("|         Gerador de senha          |")
print('+-----------------------------------+')

while not perm:
  length = input('Quantos caracteres você quer na senha? ')

  if not length.isnumeric():
    continue
  elif int(length) > 1000:
    continue
  else:
    length = int(length)
    print("\n")

    print("+-------------------------------------------------+ ")  
    print("|\\                                                 \\ ")
    print("| \\                                                 \\  ")  
    print("|   +========= Qual tipo de senha você quer =========+ ")  
    print("|  ||                                               ||")
    print("|  ||  1 -> Senha numérica                          ||")
    print("|  ||  2 -> Senha alfabética                        ||")
    print("|  ||  3 -> Senha alfanumérica                      ||")  
    print("|  ||  4 -> Senha com chars especiais               ||")  
    print("|  ||  5 -> Senha numérica com chars especiais      ||")  
    print("|  ||  6 -> Senha alfabética com chars especiais    ||")
    print(" \\ ||  7 -> Todas as opções                         || ")  
    print("  \\||_______________________________________________||")  

    while not perm:
      _type = input("\n ----> ")
      if not _type.strip().isnumeric():
        continue
      elif int(_type) < 1 or int(_type) > 7:
        continue
      else:
        _type = _type.strip()
        perm = True
        
match _type:
  case '1':
    genPass(length, nums)
  case '2':
    genPass(length, letts)
  case '3':
    genPass(length, letts, nums)
  case '4':
    genPass(length, sins)
  case '5':
    genPass(length, nums, sins)
  case '6':
    genPass(length, letts, sins)
  case '7':
    genPass(length, letts, nums, sins)

