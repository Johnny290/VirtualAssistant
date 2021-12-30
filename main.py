import Sofia as S
import e_d

e_d.getE()
x = 3
while x > 0:
    S.run()
    x-=1
    if x == 1:
        S.talk("Do you want any other help?")
        cmmd = S.take_command()
        if "yes" in cmmd:
            S.talk("Ok so what can i do for you?")
            x+=50
        else:
            break




