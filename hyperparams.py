# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
June 2017 by kyubyong park. 
kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/transformer
'''
class Hyperparams:
    '''Hyperparameters'''
    # data
    source_train = '/home/iorife/github/yoruba_asr/automatic_diacritization/seq2seq/nmt_data/yoruba_diacritics/train/sources.txt'
    target_train = '/home/iorife/github/yoruba_asr/automatic_diacritization/seq2seq/nmt_data/yoruba_diacritics/train/targets.txt'
    source_test = '/home/iorife/github/yoruba_asr/automatic_diacritization/seq2seq/nmt_data/yoruba_diacritics/dev/sources.txt'
    target_test = '/home/iorife/github/yoruba_asr/automatic_diacritization/seq2seq/nmt_data/yoruba_diacritics/dev/targets.txt'
    
    # training
    batch_size = 32 # alias = N
    lr = 0.0001 # learning rate. In paper, learning rate is adjusted to the global step.
    logdir = 'logdir' # log directory
    
    # model
    maxlen = 30 # Maximum number of words in a sentence. alias = T.
                # Feel free to increase this if you are ambitious.
    min_cnt = 1 # words whose occurred less than min_cnt are encoded as <UNK>.
    hidden_units = 512 # alias = C
    num_blocks = 6 # number of encoder/decoder blocks
    num_epochs = 200
    num_heads = 8
    dropout_rate = 0.1
    sinusoid = False # If True, use sinusoid. If false, positional embedding.
    
    
    
    
