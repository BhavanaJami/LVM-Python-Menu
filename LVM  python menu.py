print("                           Welcome to my lvmmenu                          ")
print("                          --------------------                         ")

while(True):
    print("\n")
    print("press 1: To see all the harddisks")
    print("press 2: To create physical volume")
    print("press 3: To display the physical volume")
    print("press 4: To create volume group")
    print("press 5: To display the volume group")
    print("press 6: To create logical volume")
    print("press 7: To display logical volume")
    print("press 8: To format logical volume")
    print("press 9: To create the folder")
    print("press 10: To mount the harddisk to the created folder") 
    print("press 11: To extend the logical volume size")
    print("press 12: To format the extended logical volume")
    print("\n")

    ch=int(input("                  Enter your choice:                       "))

    import os
    if ch==1:
        print("To see all the harddisks")
        os.system("fdisk -l")
    elif ch==2:
        print("To create the physical volume")
        b=input("enter harddisks to create physical volume:")
        os.system("pvcreate %s" % b)
    elif ch==3:
        print("To display the physical volume")
        c=input("enter harddisks to display physial volume:")
        os.system("pvdisplay %s" % c)
    elif ch==4:
        print("To create the volume group")
        d=input("enter the volume group name and harddisks: ")
        os.system("vgcreate %s" %d)
    elif ch==5:
        print("To display the volume group")
        e=input("enter vg name to display volume group: ")
        os.system("vgdisplay %s"% e)
    elif ch==6:
        print("TO create the logical volume")
        f=input("enter size: ")
        os.system("lvcreate --size %s --name mylv myvg" % f)
    elif ch==7:
        print("To display the logical volume")
        g=input("enter lv name to display logical volume:")
        os.system("lvdisplay %s"% g)
    elif ch==8:
        print("To format the harddisk")
        h=input("enter the disk to format:")
        os.system("mkfs.ext4 %s"% h)
    elif ch==9:
        print("To create the directory")
        i=input("enter the directory name:")
        os.system("mkdir %s"%i)
        print("Directory is created")
    elif ch==10:
        print("To mount harddisk to the created directory")
        j=input("enter disk and folder name to mount:")
        os.system("mount %s" % j)
    elif ch==11:
        print("To extend the logical volume")
        k=input("enter size to extend the logical volume:")
        os.system("lvextend --size %s /dev/myvg/mylv" %k)
    elif ch==12:
        print("To format the extended harddisk")
        l=input("enter the disk name to format after extended the size:")
        os.system("resize2fs %s" %l)
        
    else:
        print(" There is no such option")
