
import os

vec_file = {"wiki-pubmed": "./model/word2vec/wikipedia-pubmed-and-PMC-w2v.bin",
            "glove": "./model/word2vec/glove_word2vec_100d.txt"
            }

# Use Config.py to set parameters.

class Config:
    def __init__(self):
        # data
        self.data_set = "GENIA"  # ACE05 ACE04 GENIA 
        self.data_path = f"./dataset/{self.data_set}/"

        # L_{b} and IOU_{b}
        self.Lb = 10 
        self.train_neg_iou_th = 0.86  if self.data_set == "GENIA"  else 0.81 
        
        # bert
        self.use_bert = False
        self.bert_config = 'large' 
        self.fusion = True
        self.fusion_sum = True
        self.use_last_four = False
        self.input_size_bert = 768 if self.bert_config == 'base' else 1024
        self.fusion_layer = 13 if self.bert_config == 'base' else 25
        self.bert_path = "./data/bert/"

        # word embeddings
        self.vec_model = "wiki-pubmed" if self.data_set == "GENIA"  else "glove" 
        self.word_embedding_size = 100 if self.vec_model == "glove" else 200
        self.word2vec_path = vec_file[self.vec_model]


        # model
        self.use_cnn = True
        self.cnn_block = 7 if self.data_set == "GENIA" else 5
        self.kernel_size = 3  
        self.hit_pooling_size =  3
        self.nested_depth_fc_size = 1024  if self.use_bert == True else 256
        self.nested_depth = 3

        # DTE
        self.if_DTE = True
        self.if_char = True
        self.char_embedding_size = 25
        self.if_pos = True
        self.pos_embedding_size = 6 
        self.if_transformer = True
        self.N = 2
        self.h = 4
        self.if_bidirectional = True

        # train
        self.if_gpu = True
        self.if_shuffle = True
        self.if_freeze = False if self.vec_model == "glove" else True
        self.dropout = 0.5
        self.epoch = 100
        self.batch_size = 8 
        self.opt ="Adam" 
        self.lr = 3e-4
        self.score_th = 0.75

        # test
        self.if_output = False
        self.test_model_path = "./model/" + self.data_set + '/' + 'f1_0.771.pth'
     

    def __repr__(self):
        return str(vars(self))

    def get_pkl_path(self, mode):
        path = self.data_path
        if mode == "word2vec":
            path += f"word_vec"
        else:
            if mode == "config":
                path += f"config"
            else:
                path += mode + "/" \
                        + f"C_:{self.Lb}"
                if mode == "train":
                    path += f"_neg_iou_th{self.train_neg_iou_th}"

        return path + f"_{self.vec_model}.pkl"

    def get_model_path(self):
        path = f"./model/{self.data_set}"
        if not os.path.exists(path):
            os.makedirs(path)
        return path + "/"

    def get_result_path(self):
        path = f"./result/{self.data_set}"
        if not os.path.exists(path):
            os.makedirs(path)
        path += f"/{self.vec_model}"
        return path + ".data"

    def load_config(self, misc_dict):
        self.word_kinds = misc_dict["word_kinds"]
        self.char_kinds = misc_dict["char_kinds"]
        self.pos_tag_kinds = misc_dict["pos_tag_kinds"]
        self.label_kinds = misc_dict["label_kinds"]
        self.id2label = misc_dict["id2label"]
        self.id2word = None

        print(self)
        self.id2word = misc_dict["id2word"]


config = Config()
