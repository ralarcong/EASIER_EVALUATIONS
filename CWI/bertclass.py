import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM
import numpy as np


class bertclass:
    model = BertModel.from_pretrained('pytorch/')
    tokenizer = BertTokenizer.from_pretrained("pytorch/", do_lower_case=False)
    
    def __init__(self):
        self.data = []
    
    def bertvectors(self,word,sentence):
        #print(word)
        #print(sentence)
        
        text = sentence

        # Add the special tokens.
        marked_text = "[CLS] " + text + " [SEP]"

        # Split the sentence into tokens.
        tokenized_text = self.tokenizer.tokenize(marked_text)

        # Map the token strings to their vocabulary indeces.
        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)
        segments_ids = [1] * len(tokenized_text)

        tokens_tensor = torch.tensor([indexed_tokens])
        segments_tensors = torch.tensor([segments_ids])

        # Load pre-trained model (weights)
        #model = BertModel.from_pretrained('../MLESSUI/pytorch/')

        # Put the model in "evaluation" mode, meaning feed-forward operation.
        self.model.eval()

        with torch.no_grad():
            encoded_layers, _ = self.model(tokens_tensor, segments_tensors)

        token_embeddings = torch.stack(encoded_layers, dim=0)
        token_embeddings = torch.squeeze(token_embeddings, dim=1)

        token_embeddings = token_embeddings.permute(1,0,2)

        # Stores the token vectors, with shape [22 x 768]
        token_vecs_sum = []

        # `token_embeddings` is a [22 x 12 x 768] tensor.

        # For each token in the sentence...
        for token in token_embeddings:

            # `token` is a [12 x 768] tensor

            # Sum the vectors from the last four layers.
            sum_vec = torch.sum(token[-4:], dim=0)

            # Use `sum_vec` to represent `token`.
            token_vecs_sum.append(sum_vec)

        # `encoded_layers` has shape [12 x 1 x 22 x 768]

        # `token_vecs` is a tensor with shape [22 x 768]
        token_vecs = encoded_layers[11][0]

        # Calculate the average of all 22 token vectors.
        sentence_embedding = torch.mean(token_vecs, dim=0)
        
        tokenized_words = self.tokenizer.tokenize(word)
        
        wordvectorsuma=[]
        
        #if len(tokenized_words)<2:

        #   index=tokenized_text.index(word)

         #   vectores=token_vecs_sum[index][:5]
            
          #  return vectores
            

        for token in tokenized_words:
            if token in tokenized_text:
                if(len(wordvectorsuma)==0):
                    index=tokenized_text.index(token)
                    wordvectorsuma=np.array(token_vecs_sum[index][:480])
                else:
                    index=tokenized_text.index(token)
                    wordvectorsuma = wordvectorsuma+np.array(token_vecs_sum[index][:480])
            else:
                if(len(wordvectorsuma)==0):
                    wordvectorsuma = [0] * 480
                else:
                    wordvectorsuma = wordvectorsuma+np.array(0)

        wordvectorsuma = np.array(wordvectorsuma)/len(tokenized_words)

        
        return wordvectorsuma
    
    