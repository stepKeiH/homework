# coding: utf-8

import sys
import os.path
from struct import *
from array import *


def divide_8_files(input_file):
    f_input = open(input_file,'rb')

    def read_input(N, file):
        x = array('i',[])
        x.fromfile(f_input, N)
        print('input completed', file=sys.stderr)

        x = x.tolist()
        x.sort()
        f_out = open(file,'wb')

        result = array('i',[])
        result.fromlist(x)
        result.tofile(f_out)
        print('output completed', file=sys.stderr)
        f_out.close()

    for i in "ABCDEFGH":
        read_input(312500000, 'merge_'+i)

    f_input.close()

def merge_array(x, y, z):

    f_input_1 = open(x,'rb')
    f_input_2 = open(y,'rb')

    def make_list_from_file(x, f_input):
        count = 0
        x_count = 0
        x_list = []
        while count < 10000000:
            new = f_input.read(4)
            if not new:
                f_input.close()
                x_count = 1
                break
            x_list.append(unpack('i', new)[0])
            count += 1
        return x_list, count, x_count

    x_list, x_size, x_count = make_list_from_file(x, f_input_1)
    y_list, y_size, y_count = make_list_from_file(y, f_input_2)

    def merge_two_lists(x_list, x_size, x_count, y_list, y_size, y_count, z):
        x_ind = 0
        y_ind = 0
        z_array = array('i',[])
        f_add = open(z,'ab')

        while True:
            if len(z_array) > 10000000:
                z_array.tofile(f_add)
                z_array = array('i',[])
            if x_ind >= x_size - 1:
                if x_count == 0:
                    x_list, x_size, x_count = make_list_from_file(x, f_input_1)
                    x_ind = 0
                else:
                    z_array.fromlist(y_list[y_ind:])
                    break
            if y_ind >= y_size - 1:
                if y_count == 0:
                    y_list, y_size, y_count = make_list_from_file(y, f_input_2)
                    y_ind = 0
                else:
                    z_array.fromlist(x_list[x_ind:])
                    break
            if x_list[x_ind] < y_list[y_ind]:
                z_array.append(x_list[x_ind])
                x_ind += 1
            if y_list[y_ind] < x_list[x_ind]:
                z_array.append(y_list[y_ind])
                y_ind += 1
            if y_list[y_ind] == x_list[x_ind]:
                z_array.append(x_list[x_ind])
                z_array.append(y_list[y_ind])
                x_ind += 1
                y_ind += 1

        if len(z_array) > 0:
            z_array.tofile(f_add)
        f_add.close()

    merge_two_lists(x_list, x_size, x_count, y_list, y_size, y_count, z)

def main(input_file):
    divide_8_files(input_file)

    file_list = ['A','B','C','D','E','F','G','H']

    def get_file(s):
        return 'merge_'+ s

    while len(file_list) > 1:
        f_1 = file_list.pop()
        f_2 = file_list.pop()
        f_3 = f_1 + f_2
        merge_array(get_file(f_1), get_file(f_2), get_file(f_3))
        file_list.insert(0,f_3)


if __name__ == '__main__':
    main(sys.argv[1])
