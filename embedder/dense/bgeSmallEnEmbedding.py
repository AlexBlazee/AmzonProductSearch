from typing import List
from sentence_transformers import SentenceTransformer
import torch

class BgeSmallEnEmbedding:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'        
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5", device= self.device)

    def embed_query(self,query):
        dense = self.model.encode(query , convert_to_numpy= True )
        return dense
    
    def embed_documents(self, docs : List):
        dense =  self.model.encode(docs , convert_to_numpy= True)
        return dense