import tensorflow as tf
import numpy as np


# #### Following code serves for nice and smart defyning model as reusable code



    
def main():
    sess = tf.Session()
    model = Model(dataset, label)
    sess.run(tf.initialize_all_variables())
    


# In[23]:


img_size = 28
num_channels = 1
num_classes = 10
learning_rate = 1e-4
#ADD MORE PARAMETERS HERE BOI
params = {"learning_rate": learning_rate,
          "img_size": img_size,
          "num_channels":num_channels,
          "num_classes":num_classes}


if __name__ == '__main__':
    main()


# ###### trash code
# img_size_flat = int(img_size*img_size*64/16)
