import tensorflow as tf
import functools

def lazy_property(function):
    attribute = '_cache_' + function.__name__
    
    @property
    @functools.wraps(function)
    def decorator(self):
        if not hasattr(self, attribute):
            with tf.variable_scope(function.__name__):
                setattr(self, attribute, function(self))
        return getattr(self, attribute)
    
    return decorator


# ##### Data loading Block

# In[25]:




# ##### Defining model as reusable function

# In[24]:


class Model:
    
    def __init__(self, data, label, params):
        self.data = data
        self.target = target
        self.img_size = params["img_size"]
        self.num_channeles = params["num_channels"]
        self.num_classes = params["num_classes"]
        self.prediction
        self.optimize
        self.error
        
    @lazy_property
    def prediction(self):
        #INPUT LAYER
        net = tf.reshape(features["x"],[-1, img_size, img_size, num_channels])
        #1 conv layer
        net = tf.layers.conv2d(inputs = input_layer, 
                                 filters = 16,
                                 kernel_size = 5,
                                 strides = 1,
                                 padding = "same",
                                 activation = tf.nn.relu,
                                 name = "conv1")
        #1 pool layer, img size reduced by 1/4
        net = tf.layers.max_pooling2d(inputs=conv1,
                                        pool_size = 2, 
                                        strides = 2,
                                        padding = "same",
                                        name = "pool1")


        pool2_flat = tf.reshape(pool2,[-1,self])


        dense = tf.layers.dense(inputs = pool2_flat,
                                units = 128,
                                activation = tf.nn.relu)

        dense2 = tf.layers.dense(inputs = dense,
                                 units = 64,
                                 activation = tf.nn.relu)

        logits = tf.layers.dense(inputs = dense2,
                                 units = num_classes,
                                 activation = tf.nn.relu)




        # Softmax output of the neural network.
        #[10,x] tesnor
        y_pred = tf.nn.softmax(logits=logits)
        return 
    
    
    
    @lazy_property
    def optimize(self):
        cross_entropy = -tf.reduce_sum(self.target, tf.log(self.prediction))
        optimizer = tf.train.RMSPropOptimizer(0.03)
        return optimizer.minimize(cross_entropy)

    @lazy_property
    def error(self):
        mistakes = tf.not_equal(
            tf.argmax(self.label, 1), tf.argmax(self.prediction, 1))
        return tf.reduce_mean(tf.cast(mistakes, tf.float32))
    
    