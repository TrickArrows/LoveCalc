import random


print("STONE?PAPER?SISSOR!\n..... 5 TURNS .....\n");

u=0
c=0
for i in range(5):
    user=input("Enter Your Choice [r/p/s]\nRock[r] Paper[p] Scissor[s] -  ")
    comp=random.choice(['r','p','s'])
    print(f"COMPUTER {comp}-{user} YOU")
    while comp!=user:
        if ((comp=='r' and user=='p')or(comp=='p' and user=='s')or(comp=='s' and user=='r')):
            st1=random.choice(['you won','Nice guess','u got 1 point','oops'])
            print(st1,"\n")
            u=u+1
            break
        elif ((comp=='p' and user=='r')or(comp=='s' and user=='p')or(comp=='r' and user=='s')):
            st2=random.choice(['you lose','better luck next time','1 got 1 point','sorry'])
            print(st2,"\n")
            c=c+1
            break
        else:
            err=random.choice(['invaied choice','fool','Enter correct choice',' pls choose the correct!!'])
            print(err,"\n")
            break
    else:
        tie=random.choice(['Try again','same to you','tie'])
        print(tie,"\n\n")
print(f"......................\n  Final Result \ncomputer= {c} \nuser  = {u}\n......................")
