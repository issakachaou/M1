'Cours no. 1 : 14 septembre

'Transformation de chiffre en caractère sous condition

SI(ALEA.ENTRE.BORNES(1;2)=1;"M";"F")

'Fonction de SI impriqué

SI(ALEA.ENTRE.BORNES(1;3)=1;"A";SI(ALEA.ENTRE.BORNES(1;3)=2;"B";"C"))

'Alternative plus simple au SI impriqué

=CHOISIR(ALEA.ENTRE.BORNES(1;3);"A";"B";"C")

'Fonction rechecheV "Vlookup"

=RECHERCHEV(D2;NIVEAU!$A$2:$C$4;2;FAUX)

'faire un indentifiant avec la fonction CONCATENER

=CONCATENER(B2;D2;E2)

'faire un indentifiant de manière plus simple 

=B2&D2&E2

=STXT(A2;NBCAR(A2);1)