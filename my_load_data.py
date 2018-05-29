
# coding: utf-8

# In[35]:


import sys
import os
import numpy as np
from six.moves import cPickle as pickle


# In[36]:


def load_dataset_fn(mode,src_dir="./data", file_name='Train.pickle',img_size = 256, num_channels = 3 ,num_classes = 2):
    """mode = test for test data,
    valid for validation data,
    train for training data,
    src_dir = "./data"
    file_name = "Test.pickle """
    # coding: utf-8
    #Import data from notMNIST file
    if mode == 'train' or mode == 'valid' or mode == 'test' :
        name_dataset = mode + '_dataset'
        name_label = mode + '_labels'
        pickle_file = os.path.join(src_dir,file_name)
        with open(pickle_file, 'rb') as f:
            save = pickle.load(f)
        return save #labels
    else:
        print("bad mode")
        return null
    

