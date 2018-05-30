import sys
import os
import numpy as np
from six.moves import cPickle as pickle

def load_dataset_fn(mode, src_dir="./data"):
    """mode = "train" or "test", returns dataset, labels for given mode """
    if mode == 'train' or mode == 'test' :
        file_name = "Dataset.pickle"
        pickle_file = os.path.join(src_dir,file_name)
        mode_labels = mode + "_labels"
        mode_dataset = mode + "_dataset"
        with open(pickle_file, 'rb') as f:
            save = pickle.load(f)
            dataset = save[mode_dataset]
            labels = save[mode_labels]
            del save
        return dataset, labels
    else:
        print("Bad mode")
        return null
    

