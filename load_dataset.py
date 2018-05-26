def load_dataset_fn(mode, file_name = 'notMNIST.pickle'):
    """mode = test for test data, 
    valid for validation data,
    train for training data,
    file_name = 'notMNIST.pickle' """
    img_size = 28
    import sys
    import os
    import numpy as np
    from six.moves import cPickle as pickle
    # coding: utf-8
    #Import data from notMNIST file
    if mode == 'train' or mode == 'valid' or mode == 'test' :
        name_dataset = mode + '_dataset'
        name_label = mode + '_labels'
        pickle_file = file_name

        with open(pickle_file, 'rb') as f:
            save = pickle.load(f)
            dataset = save[name_dataset]
            labels = save[name_label]

            del save  # hint to help gc free up memory

        dataset = dataset.reshape(
            (-1, img_size, img_size, num_channels)).astype(np.float32)
        labels = (np.arange(num_classes) == labels[:,None]).astype(np.float32)

        return dataset, labels
    else:
        print("bad mode")
        return null
    
    
    
    
    
    
    """
        train_dataset, train_labels = reformat(train_dataset, train_labels)
        valid_dataset, valid_labels = reformat(valid_dataset, valid_labels)
        test_dataset, test_labels = reformat(test_dataset, test_labels)
        print('Training set', train_dataset.shape, train_labels.shape)
        print('Validation set', valid_dataset.shape, valid_labels.shape)
        print('Test set', test_dataset.shape, test_labels.shape) """