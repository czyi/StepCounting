#! /usr/bin/env python
# coding=utf-8
import os
import shutil
import time
import types 
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


def copy_and_rename(fpath_input, fpath_output):
    folder_list = []
    for folder in os.listdir(fpath_input):
        folder_name = os.path.splitext(folder)[0]
        # print(type(folder_name))
        # print(folder_name)
        folder_list.append(fpath_input+'/'+folder_name+"/iPhone6-1L")
        folder_list.append(fpath_input+'/'+folder_name+"/iPhone6-2R")

    print(len(folder_list))

    for folder_path in folder_list:
        for folder in os.listdir(folder_path):
            if(folder[0]!='T'):
                continue
            print(folder)
            for file in os.listdir(folder_path+'/'+folder):
                if(file=='iPhoneSensors.csv'):
                    # print('\t', file)
                    oldname = os.path.join(folder_path+'/'+folder, file)
                    newname = os.path.join(fpath_output+'/sensor', os.path.splitext(file)[0]+'_'+folder+".csv")
                    print(oldname)
                    print(newname)
                    shutil.copy(oldname, newname)
        print('===========')



        # #if os.path.splitext(file)[1] == ".jpg":
        # oldname = os.path.join(fpath_input, file)
        # newname_1 = os.path.join(fpath_output,
        #                          os.path.splitext(file)[0] + "_1.jpg")
        # newname_2 = os.path.join(fpath_output,
        #                          os.path.splitext(file)[0] + "_2.jpg")
        # newname_3 = os.path.join(fpath_output,
        #                          os.path.splitext(file)[0] + "_3.jpg")
        # #os.rename(oldname, newname)
        # shutil.copyfile(oldname, newname_1)
        # shutil.copyfile(oldname, newname_2)
        # shutil.copyfile(oldname, newname_3)


if __name__ == '__main__':
    print('start ...')
    t1 = time.time() * 1000
    #time.sleep(1) #1s
    fpath_input = "/home/ziyi/projects/ark+=b7291=d17p46_version_5/WeAllWalkv4/WeAllWalkToPublish8-20-17/SENSORDATA"
    fpath_output = "~/projects/test"
    copy_and_rename(fpath_input, fpath_output)
    t2 = time.time() * 1000
    print('take time:' + str(t2 - t1) + 'ms')
    print('end.')

