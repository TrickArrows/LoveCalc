import random
print("LOVE CALCULATER\nI'm The Best Calc. In The World\n");
def love():
    n1=input("Enter your Name: ");
    n2=input("Enter your crush: ");

    if len(n1)>=1 and len(n2)>=1:
        persentage=random.randint(1,100);
        if persentage==100:
            print("You are the best lovers in the world!!!");
    else:
        print("\n enter the names correctly\ntry again!!\n\n");
        love();
    print(f"\n {n1} Loves {n2} =",persentage,"% \n\n");

    love();
love();
