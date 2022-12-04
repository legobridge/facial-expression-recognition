from matplotlib import image
from matplotlib import pyplot as plt
import pandas as pd

from PIL import Image
  
df_bound_test = pd.read_csv("data/Annotation/boundingbox/bb_test.csv")
df_bound_train = pd.read_csv("data/Annotation/boundingbox/bb_train.csv")

df_autostd_train = pd.read_csv("data/Annotation/auto/vansh.csv")

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

        # Aligned Auto Test Annotation

        # Aligned Manual Test Annotation

        # Aligned Test Bounding Box


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
        

        # Aligned Manual Train Annotation

        # Aligned Train Bounding Box

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






# if w == 'A':
#     if q == 'Te':
#         file_auto_test = open("data/basic/Annotation/auto/test_" + str(x) + "_auto_attri.txt","r+") 
#         l = [file_auto_test.read()]
#         file_auto_test.close()
#         r = []
#         for i in l:
#             r.append(i.split())
#         z = r[0]
#     else:
#         file_auto_train = open("data/basic/Annotation/auto/train_" + str(x) + "_auto_attri.txt","r+") 
#         l2 = [file_auto_train.read()]
#         file_auto_train.close()
#         r2 = []
#         for j in l2:
#             r2.append(j.split())
#         z = r2[0]
       


# else:
#     if q == 'Te':
#         file_manual_test = open("data/basic/Annotation/manual/test_" + str(x) + "_manu_attri.txt","r+") 
#         l = [file_manual_test.read()]
#         file_manual_test.close()
#         r = []
#         for i in l:
#             r.append(i.split())
#         z = r[0]
#         z = z[:len(z)-3]
#     else:
#         file_manual_train = open("data/basic/Annotation/manual/train_" + str(x) + "_manu_attri.txt","r+") 
#         l2 = [file_manual_train.read()]
#         file_manual_train.close()
#         r2 = []
#         for j in l2:
#             r2.append(j.split())
#         z = r2[0]
#         z = z[:len(z)-3]

# Bounding Box    
# if y == 'o':
#     if q == 'Te':
#         row_bb_test = df_bound_test[df_bound_test['id'] == int(x)]
#         l_bb = row_bb_test.values.tolist()
#         l_bb = l_bb[0][1:]
#     elif q == 'Tr':
#         row_bb_train = df_bound_train[df_bound_train['id'] == int(x)]
#         l_bb = row_bb_train.values.tolist()
#         l_bb = l_bb[0][1:]
# else:
#     row = df_autostd_train[df_autostd_train['id'] == int(x)]
#         # print(row)
#     l_new = row.values.tolist()
#     l_new = l_new[0][1:]
#     for i in range(0,len(l_new),2):
#         plt.plot((float(l_new[i]))*100,(float(l_new[i+1]))*100, marker='o', color="red")
#         plt.imshow(v)
#     plt.show()
# Train data(z2) + Train Image(v2)
# for i in range(0,len(z2),2):
#     plt.plot(float(z2[i]),float(z2[i+1]), marker='o', color="yellow", markersize=1)
#     plt.imshow(v2)
# plt.show()


    
    

# r = [153.841080, 130.382935, 327.412231, 355.140106] 
# for i in range(0,len(r),2):
#     plt.plot(float(z2[i]),float(z2[i+1]), marker='o', color="red", markersize=1)
#     plt.imshow(v)
# plt.show()

# print("unscaled:",z)
# amin, amax = 0, width
# amin2, amax2 = 0, height

# for i in range(0,len(z),2):
#     z[i] = (float(z[i])/(amax-amin))*100
#     z[i+1] = (float(z[i+1])/(amax2-amin2))*100
# data_aligned_test_num = image.imread('data/basic/Image/aligned/test_00' + str(x) + '_aligned.jpg')
# v = data_aligned_test_num

# print("scaled:",z)

# for i in range(0,len(z),2):
#     plt.plot(float(z[i]),float(z[i+1]), marker='o', color="red")
#     plt.imshow(v)
# plt.show()




# # Train data(z2) + Test Image(v)
# for i in range(0,len(z2),2):
#     plt.plot(float(z2[i]),float(z2[i+1]), marker='v', color="yellow")
#     plt.imshow(v)
# plt.show()

# # Test data(z) + Train Image(v2)
# for i in range(0,len(z),2):
#     plt.plot(float(z[i]),float(z[i+1]), marker='v', color="red")
#     plt.imshow(v2)
# plt.show()



# # Test 1
# # Original and Manual works
# plt.plot(96.460, 84.143, marker='v', color="red")
# plt.imshow(data)
# plt.show()


# # Test 2 
# # Original and Automatic do not work
# # plt.plot(248, 290, marker='v', color="red")
# # plt.imshow(data)
# # plt.show()


# # Test 3
# # Aligned and Manual do not work
# manual11_1 = [44.444,	45.646, 58.959,	46.446,	51.552,	55.155,	43.243,	57.958,	56.857,	58.859]
# for i in range(0,len(manual11_1),2):
#     print(manual11_1[i],manual11_1[i+1])
#     plt.plot(manual11_1[i], manual11_1[i+1], marker='v', color="red")
#     plt.imshow(data_aligned11)
#     # plt.imshow(data11)

# plt.show()

# # plt.plot(96.460, 84.143, marker='v', color="red")
# # plt.imshow(data_aligned)
# # plt.show()


# # Test 4
# # Aligned and Automatic_train do not work
# auto_11_1 =	[36,	41,	41,	40.5,	46,	41,	54,	42,	58.5,	40.5,	63,	42,	50,	44,	50,	53,	45,	53,	47,	55,	50,	56,	53,	55,	55,	53,	39,	43,	40,	43,	44,	43	,46, 44, 44, 45,	40,	44,	54,	44,	56,	43,	59,	43,	61,	44,	60,	44,	56,	45,	43,	58,	45,	57,	48,	58,	50,	58,	51,	58,	55,	58,	57,	58,	55,	61,	52,	63,	49,	63,	46,	63,	44,	60]
# auto_11_2 = [156,144,183,138,209,145,229,146,	242,	138.5,	253,	140,	214.5,	159,	226,	199,	198,	198,	209,	205,	219,	208,	229,	205,	232,	197,	167,	159,	175,	155,	191,	155,	197,	161,	191,	163,	173,	163,	225,	159,	230,	152,	243,	152,	247,	157,	244,	160,	230,	161,	185,	225,	196,	220,	209,	217,	216,	218,	222,	217,	226,	219,	223,	224,	223,	232,	219,	241,	212,	246,	199,	244,	190,	235]
# for i in range(0,len(auto_11_1),2):
#     print(auto_11_1[i],auto_11_1[i+1])
#     plt.plot(auto_11_1[i], auto_11_1[i+1], marker='v', color="red")
#     plt.imshow(data_aligned11)
#     # plt.imshow(data11)
# plt.show()

# # Original and Automatic_test work
# for i in range(0,len(auto_11_2),2):
#     print(auto_11_2[i],auto_11_2[i+1])
#     plt.plot(auto_11_2[i], auto_11_2[i+1], marker='v', color="red")
#     plt.imshow(data_aligned11)
#     plt.imshow(data11)
# plt.show()
# for i in range(0,len(z),2):
#     plt.plot(float(z[i]),float(z[i+1]), marker='v', color="red")
#     plt.imshow(data_test_num)
#     # plt.imshow(data11)
# plt.show()

# plt.plot(248, 290, marker='v', color="red")
# plt.imshow(data_aligned)
# plt.show()


# Test 5 
# Original and Manual works (Image 11)
# plt.plot(184.293, 159.993, marker='v', color="red")
# plt.imshow(data11)
# plt.show()

# Test 6
# Aligned and Automatic do not work
# plt.plot(36, 41, marker='v', color="red")
# plt.plot(41, 40.5, marker='v', color="red")
# plt.plot(46, 41, marker='v', color="red")
# plt.plot(54, 42, marker='v', color="red")
# plt.plot(54, 42, marker='v', color="red")



# # Auto
# # plt.imshow(data_aligned_num)

# # Manual
# plt.imshow(data11 )


# plt.show()


