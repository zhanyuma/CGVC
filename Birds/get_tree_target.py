import numpy as np
import torch
from torch.autograd import Variable
import torch.nn as nn

trees = [
[1,12,35],
[2,12,35],
[3,12,35],
[4,6,9],
[5,4,4],
[6,4,4],
[7,4,4],
[8,4,4],
[9,8,18],
[10,8,18],
[11,8,18],
[12,8,18],
[13,8,18],
[14,8,13],
[15,8,13],
[16,8,13],
[17,8,13],
[18,8,26],
[19,8,21],
[20,8,19],
[21,8,24],
[22,3,3],
[23,13,37],
[24,13,37],
[25,13,37],
[26,8,18],
[27,8,18],
[28,8,14],
[29,8,15],
[30,8,15],
[31,6,9],
[32,6,9],
[33,6,9],
[34,8,16],
[35,8,16],
[36,10,33],
[37,8,30],
[38,8,30],
[39,8,30],
[40,8,30],
[41,8,30],
[42,8,30],
[43,8,30],
[44,13,38],
[45,12,36],
[46,1,1],
[47,8,16],
[48,8,16],
[49,8,18],
[50,11,34],
[51,11,34],
[52,11,34],
[53,11,34],
[54,8,13],
[55,8,16],
[56,8,16],
[57,8,13],
[58,4,4],
[59,4,5],
[60,4,5],
[61,4,5],
[62,4,5],
[63,4,5],
[64,4,5],
[65,4,5],
[66,4,5],
[67,2,2],
[68,2,2],
[69,2,2],
[70,2,2],
[71,4,6],
[72,4,6],
[73,8,15],
[74,8,15],
[75,8,15],
[76,8,24],
[77,8,30],
[78,8,30],
[79,5,7],
[80,5,7],
[81,5,7],
[82,5,7],
[83,5,7],
[84,5,8],
[85,8,11],
[86,7,10],
[87,1,1],
[88,8,18],
[89,1,1],
[90,1,1],
[91,8,21],
[92,3,3],
[93,8,15],
[94,8,27],
[95,8,18],
[96,8,18],
[97,8,18],
[98,8,18],
[99,8,23],
[100,9,32],
[101,9,32],
[102,8,30],
[103,8,30],
[104,8,22],
[105,3,3],
[106,4,4],
[107,8,15],
[108,8,15],
[109,8,23],
[110,6,9],
[111,8,20],
[112,8,20],
[113,8,24],
[114,8,24],
[115,8,24],
[116,8,24],
[117,8,24],
[118,8,25],
[119,8,24],
[120,8,24],
[121,8,24],
[122,8,24],
[123,8,24],
[124,8,24],
[125,8,24],
[126,8,24],
[127,8,24],
[128,8,24],
[129,8,24],
[130,8,24],
[131,8,24],
[132,8,24],
[133,8,24],
[134,8,28],
[135,8,17],
[136,8,17],
[137,8,17],
[138,8,17],
[139,8,13],
[140,8,13],
[141,4,5],
[142,4,5],
[143,4,5],
[144,4,5],
[145,4,5],
[146,4,5],
[147,4,5],
[148,8,24],
[149,8,21],
[150,8,21],
[151,8,31],
[152,8,31],
[153,8,31],
[154,8,31],
[155,8,31],
[156,8,31],
[157,8,31],
[158,8,23],
[159,8,23],
[160,8,23],
[161,8,23],
[162,8,23],
[163,8,23],
[164,8,23],
[165,8,23],
[166,8,23],
[167,8,23],
[168,8,23],
[169,8,23],
[170,8,23],
[171,8,23],
[172,8,23],
[173,8,23],
[174,8,23],
[175,8,23],
[176,8,23],
[177,8,23],
[178,8,23],
[179,8,23],
[180,8,23],
[181,8,23],
[182,8,23],
[183,8,23],
[184,8,23],
[185,8,12],
[186,8,12],
[187,10,33],
[188,10,33],
[189,10,33],
[190,10,33],
[191,10,33],
[192,10,33],
[193,8,29],
[194,8,29],
[195,8,29],
[196,8,29],
[197,8,29],
[198,8,29],
[199,8,29],
[200,8,23]
]



trees_order_to_family = [ 
[1,1],
[2,2],
[3,3],
[4,4,5,6],
[5,7,8],
[6,9],
[7,10],
[8,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
[9,32],
[10,33],
[11,34],
[12,35,36],
[13,37,38],
]


trees_family_to_species = [ 
[1, 46, 87, 89, 90],
[2, 67, 68, 69, 70],
[3, 22, 92, 105],
[4, 5, 6, 7, 8, 58, 106],
[5, 59, 60, 61, 62, 63, 64, 65, 66, 141, 142, 143, 144, 145, 146, 147],
[6, 71,72],
[7, 79, 80, 81, 82, 83],
[8, 84],
[9, 4, 31, 32, 33, 110],
[10, 86],
[11, 85],
[12, 185, 186],
[13, 14,15,16,17, 54, 57, 139, 140],
[14, 28],
[15, 29, 30, 73, 74, 75, 93, 107, 108],
[16, 34, 35, 47, 48, 55, 56],
[17, 135, 136, 137, 138],
[18,9,10,11,12,13, 26, 27, 49, 88, 95, 96, 97, 98],
[19, 20],
[20, 111, 112],
[21, 19, 91, 149, 150],
[22, 104],
[23, 99, 109,  158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171,\
 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 200],
[24, 21, 76, 113, 114, 115, 116, 117, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131\
, 132, 133, 148],
[25, 118],
[26, 18],
[27, 94],
[28, 134],
[29, 193, 194, 195, 196, 197, 198, 199],
[30, 37, 38, 39, 40, 41, 42, 43, 77, 78, 102, 103],
[31, 151, 152, 153, 154, 155, 156, 157],
[32, 100, 101],
[33, 36, 187, 188, 189, 190, 191, 192],
[34, 50, 51, 52, 53],
[35, 1, 2, 3],
[36, 45],
[37, 23,24,25],
[38, 44],
]




trees_order_to_species = [
[1, 46, 87, 89, 90], 
[2, 67, 68, 69, 70], 
[3, 22, 92, 105],
[4, 5, 6, 7, 8, 58, 106, 59, 60, 61, 62, 63, 64, 65, 66, 141, 142, 143, 144, 145, 146, 147, 
71,72],  #1
[5, 79 , 80 , 81 , 82 , 83, 84],  #1
[6, 4, 31, 32, 33, 110],

[7, 86],
[8, 85, 
185, 186, 
14,15,16,17,54,57,139,140, 
28, 
29,30,73,74,75,93,107,108, 
34,35,47,48,55,56, 
135,136,137,138, 
9,10,11,12,13,26,27,49,88,95,96,97,98, 
20, 
111,112, 
19,91,149,150, 
104, 
99, 109, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 200, 
21, 76, 113, 114, 115, 116, 117, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 148, 
118, 
18, 
94, 
 193, 194, 195, 196, 197, 198, 199, 
37, 38, 39, 40, 41, 42, 43, 77, 78, 102, 103,
151, 152, 153, 154, 155, 156, 157
],  #1
[9, 100, 101],
[10, 36, 187, 188, 189, 190, 191, 192],  #1
[11, 50, 51, 52, 53],
[12, 1,2,3,45],#1
[13, 23,24,25,44]
]

def get_order_family_target(targets):


    order_target_list = []
    family_target_list = []


    for i in range(targets.size(0)):

        order_target_list.append(trees[targets[i]][1]-1)
        family_target_list.append(trees[targets[i]][2]-1)



    order_target_list = Variable(torch.from_numpy(np.array(order_target_list)).cuda())   
    family_target_list = Variable(torch.from_numpy(np.array(family_target_list)).cuda())   

    return order_target_list, family_target_list




def get_order_to_family_target(targets, Temp ):


    order_to_family_target_list = []


    for i in range(targets.size(0)):

        w = torch.tensor([Temp[i]] * 38)
        index = [i - 1 for i in trees_order_to_family[targets[i]][1:]]
        w[index] = 1
        temp = w
        #temp = list(set(list(range(38))) - set(temp))
        temp = Variable(torch.from_numpy(np.array(temp)).cuda())

        order_to_family_target_list.append(temp.unsqueeze(0))

    order_to_family_target_list = torch.cat(order_to_family_target_list, 0)

    return order_to_family_target_list

def get_order_to_species_target(targets, Temp ):


    order_to_species_target_list = []


    for i in range(targets.size(0)):

        w = torch.tensor([Temp[i]] * 200)
        index = [i -1 for i in trees_order_to_species[targets[i]][1:]]
        w[index] = 1
        temp = w
        #temp = list(set(list(range(200))) - set(temp))
        temp = Variable(torch.from_numpy(np.array(temp)).cuda())

        order_to_species_target_list.append(temp.unsqueeze(0))
    order_to_species_target_list = torch.cat(order_to_species_target_list, 0)

    return order_to_species_target_list

def get_family_to_species_target(targets, Temp):


    family_to_species_target_list = []


    for i in range(targets.size(0)):

        w = torch.tensor([Temp[i]] * 200)

        index = [i - 1 for i in trees_family_to_species[targets[i]][1:]]
        w[index] = 1
        temp = w
        #temp = list(set(list(range(200))) - set(temp))
        temp = Variable(torch.from_numpy(np.array(temp)).cuda())

        family_to_species_target_list.append(temp.unsqueeze(0))

    family_to_species_target_list = torch.cat(family_to_species_target_list, 0)

    return family_to_species_target_list


def get_tree_target(pair_1, pair_2):

    tree_target_list = []


    for i in range(pair_1.size(0)):

        if trees[pair_1[i]][0] == trees[pair_2[i]][0]:
            tree_target_list.append(3)

        elif trees[pair_1[i]][1] == trees[pair_2[i]][1] and trees[pair_1[i]][2] == trees[pair_2[i]][2]:
            tree_target_list.append(2)

        elif trees[pair_1[i]][1] == trees[pair_2[i]][1]:
            tree_target_list.append(1)

        else:
            tree_target_list.append(0)



    tree_target_list = Variable(torch.from_numpy(np.array(tree_target_list)).cuda())   
    

    return tree_target_list


def get_tree_target(pair_1, pair_2):

    tree_target_list = []


    for i in range(pair_1.size(0)):

        if trees[pair_1[i]][0] == trees[pair_2[i]][0]:
            tree_target_list.append(3)

        elif trees[pair_1[i]][1] == trees[pair_2[i]][1] and trees[pair_1[i]][2] == trees[pair_2[i]][2]:
            tree_target_list.append(2)

        elif trees[pair_1[i]][1] == trees[pair_2[i]][1]:
            tree_target_list.append(1)

        else:
            tree_target_list.append(0)



    tree_target_list = Variable(torch.from_numpy(np.array(tree_target_list)).cuda())   
    

    return tree_target_list


def get_tree_target_2(t):

    t_order_list = []
    t_family_list = []
    t_species_list = []

    for i in range(t.size(0)):

        if t[i] == 0:
            t_order_list.append(0)
            t_family_list.append(0)
            t_species_list.append(0)

        if t[i] == 1:
            t_order_list.append(1)
            t_family_list.append(0)
            t_species_list.append(0)

        if t[i] == 2:
            t_order_list.append(1)
            t_family_list.append(1)
            t_species_list.append(0)

        if t[i] == 3:
            t_order_list.append(1)
            t_family_list.append(1)
            t_species_list.append(1)
    
    t_order_list = Variable(torch.from_numpy(np.array(t_order_list)).cuda())
    t_family_list = Variable(torch.from_numpy(np.array(t_family_list)).cuda())  
    t_species_list = Variable(torch.from_numpy(np.array(t_species_list)).cuda())

    return t_order_list, t_family_list, t_species_list