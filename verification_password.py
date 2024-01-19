#systeme de verification de password
password= input("Entrer votre Mot de passe: ")
pass_length=len(password)
print(pass_length)
#verification si le mdp est<8
if pass_length<8 :
  print("mot de passe tro court !")
elif 8<pass_length<12 :
  print("mot de passe moyenne !")
else :
  print("mot de passe parfait !")