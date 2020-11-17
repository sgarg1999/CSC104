#!/usr/bin/env python
# coding: utf-8

# In[4]:


def read_csv(fname):
    '''
    Returns two values:

    (1) a List of str representing the headers of the .csv file

    (2) List of List of values, based on the provided .csv file
    with filename fname.

    The format of this returned list of vlaues
    is demonstrated in the following example.
    For demographic.csv, which looks like the
    following when you open it
    in Notepad, or any other simple text editor:


    Name, Age, Sex
    Bob, 22, M
    Mary, 21, F
    Joe, 28, M


    Then read_csv("demographic.csv") would return:

    (1) ["Name", "Age", "Sex"]

    (2)
    
    [
        [Bob, Mary, Joe],
        [22,  21,   28],
        [M,   F,    M]
    ]

    Note that this function assumes the .csv file has a header at the top
    indicating the column names.
    
    '''
    
    f = open(fname, 'r')    

    header = f.readline().split(',')
    num_cols = len(header)
    return_vals = []
    for i in range(num_cols):
        return_vals.append([])
        header[i] = header[i].strip()

    for line in f:
        items = line.strip().split(',')
        for i in range(len(items)):
            return_vals[i].append(items[i].strip())
    
    f.close()

    return header, return_vals

if __name__ == "__main__":
    # example call below
    header, return_vals = read_csv('demographic.csv')
    print(header)
    print(return_vals)

