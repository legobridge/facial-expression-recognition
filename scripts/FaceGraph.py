from matplotlib import image
from matplotlib import pyplot as plt
import pandas as pd
  
df_bound_test = pd.read_csv("../data/Annotation/boundingbox/bb_test.csv")
df_bound_train = pd.read_csv("../data/Annotation/boundingbox/bb_train.csv")

df_autostd_train = pd.read_csv("../data/Annotation/auto/auto_test.csv")

flag = 1
while flag == 1:
    q  = input('Enter Tr for Train, Te for Test:')
    if q == 'Tr':
        x = input('Enter Image Number between 1 to 12271:')
        if int(x) > 12271:
            print("No image with such number. Throwing error")
        else:
            le_x = len(str(x))
            for i in range(le_x,5):
                x = str(0) + str(x)
            y = input('Enter Image Type - o or a:')
            if (y == 'o') or (y == 'a'):
                flag = 0
            else:
                print("Wrong input. Re-enter:")

    else:
        x = input('Enter Image Number between 1 to 3068:')
        if int(x) > 3068:
            print("No image with such number. Throwing error")
        else:
            le_x = len(str(x))
            for i in range(le_x,4):
                x = str(0) + str(x)
            y = input('Enter Image Type - o or a:')
            if (y == 'o') or (y == 'a'):
                flag = 0
            else:
                print("Wrong input. Re-enter")

# Aligned Image
if y == 'a':

    # Mising files
    z2 = [1,1]
    l_bb = [1,1]

    # Test
    if q == 'Te':
        # Image
        data_aligned_test_num = image.imread('data/basic/Image/aligned/test_' + str(x) + '_aligned.jpg')
        v = data_aligned_test_num

    # Train
    else:
        # Image
        data_aligned_train_num = image.imread('data/basic/Image/aligned/train_' + str(x) + '_aligned.jpg')
        v = data_aligned_train_num

        # Aligned Auto Train Annotation
        row = df_autostd_train[df_autostd_train['id'] == int(x)]
        l_new = row.values.tolist()
        z = l_new[0][1:]
        for i in range(len(z)):
            z[i] = float(z[i])*100
        

# Original Image
else:

    # Test
    if q == 'Te':
        # Image
        data_test_num = image.imread('data/basic/Image/original/test_' + str(x) + '.jpg')
        v = data_test_num

        # Auto Test Annotation
        file_auto_test = open("data/basic/Annotation/auto/test_" + str(x) + "_auto_attri.txt","r+") 
        l = [file_auto_test.read()]
        file_auto_test.close()
        r = []
        for i in l:
            r.append(i.split())
        z = r[0]

        # Manual Test Annotation
        file_manual_test = open("data/basic/Annotation/manual/test_" + str(x) + "_manu_attri.txt","r+") 
        l = [file_manual_test.read()]
        file_manual_test.close()
        r = []
        for i in l:
            r.append(i.split())
        z2 = r[0]
        z2 = z2[:len(z2)-3]

        # Test Bounding Box
        row_bb_test = df_bound_test[df_bound_test['id'] == int(x)]
        l_bb = row_bb_test.values.tolist()
        l_bb = l_bb[0][1:]

    # Train
    else:
        # Image
        data_train_num = image.imread('data/basic/Image/original/train_' + str(x) + '.jpg')
        v = data_train_num

        # Auto Train Annotation
        file_auto_train = open("data/basic/Annotation/auto/train_" + str(x) + "_auto_attri.txt","r+") 
        l2 = [file_auto_train.read()]
        file_auto_train.close()
        r2 = []
        for j in l2:
            r2.append(j.split())
        z = r2[0]

        # Manual Train Annotation
        file_manual_train = open("data/basic/Annotation/manual/train_" + str(x) + "_manu_attri.txt","r+") 
        l2 = [file_manual_train.read()]
        file_manual_train.close()
        r2 = []
        for j in l2:
            r2.append(j.split())
        z2 = r2[0]
        z2 = z2[:len(z2)-3]

        # Train Bounding Box
        row_bb_train = df_bound_train[df_bound_train['id'] == int(x)]
        l_bb = row_bb_train.values.tolist()
        l_bb = l_bb[0][1:]

if y == 'o':
# Manual Annotation
    for i in range(0,len(z2),2):
        plt.plot(float(z2[i]),float(z2[i+1]), marker='o', color="red", markersize=1)
        plt.imshow(v)
    plt.show()

# Auto Annotation
for i in range(0,len(z),2):
    plt.plot(float(z[i]),float(z[i+1]), marker='o', color="red", markersize=1)
    plt.imshow(v)
# plt.show()

if y == 'o':
# Bounding Box
    for i in range(0,len(l_bb),2):
        plt.plot((float(l_bb[i])),(float(l_bb[i+1])), marker='o', color="red")
        plt.imshow(v)
plt.show()