import sys
import os
import numpy as np
from six.moves import cPickle as pickle

def load_dataset_fn(nth, src_dir="./data"):
    nth=str(int(nth))
    src_dir = os.path.join(src_dir,"Dataset")
    name = "Part"+nth
    label_name = name+".npy"
    dataset_name = name+".pickle"
    pickle_file = os.path.join(src_dir,dataset_name)
    label_name = os.path.join(src_dir,label_name)
    try:
        with open(pickle_file, 'rb') as f:
            dataset = pickle.load(f)
            labels = np.load(label_name)
        dataset,labels = randomize(dataset,labels)
        return dataset, labels
    except Exception as e:
        print('Unable to save data to', pickle_file, ':', e)
        raise

def randomize(dataset, labels):
    permutation = np.random.permutation(labels.shape[0])
    shuffled_dataset = dataset[permutation,:,:]
    shuffled_labels = labels[permutation]
    return shuffled_dataset, shuffled_labels
