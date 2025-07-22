# implement long term memory for the agent
import numpy as np
from faiss import IndexFlat, VectorStoreIndex
from typing import List, Dict, Any

class LongTermMemory:
    def __init__(self):
        self.memories = []  # List to store memory objects
        self.vector_index = None  # For efficient vector similarity search
        
    class Memory:
        def __init__(self, content: str, metadata: Dict[str, Any] = {}):
            self.content = content
            self.metadata = metadata
            
    def add_memory(self, content: str, metadata: Dict[str, Any] = {}):
        """Add a new memory"""
        memory = LongTermMemory.Memory(content, metadata)
        self.memories.append(memory)
        
    def store_document(self, document_content: str, doc_id: str = None, 
                      metadata: Dict[str, Any] = {}):
        """Store a document for future reference"""
        # Split into chunks if needed (you can implement chunking logic here)
        # For now, storing full content
        memory = LongTermMemory.Memory(document_content, {
            'doc_id': doc_id,
            **metadata
        })
        self.memories.append(memory)
        
    def retrieve(self, query: str) -> List[Dict[str, Any]]:
        """Retrieve relevant memories based on query string"""
        # For efficient retrieval, we'll use vector similarity search
        # Implement embedding generation for both query and stored memories
        
        # Convert all stored memories to embeddings and create index if not done yet
        if self.vector_index is None:
            self._initialize_vector_storage()
            
        # Generate query embedding (simplified as example)
        query_embedding = self._compute_embedding(query)
        
        # Search for similar vectors
        similarities = self.vector_index.search([query_embedding])
        
        # Get indices of top matches
        results = []
        for idx, score in zip(similarities[1][0], similarities[0][0]):
            result = {
                'content': self.memories[idx].content,
                'metadata': self.memories[idx].metadata,
                'similarity_score': score
            }
            results.append(result)
            
        return results
    
    def _initialize_vector_storage(self):
        """Initialize vector storage with existing memories"""
        # Convert all memories to embeddings and store in index
        if not self.memories:
            return
            
        # Assuming embedding dimension is 300 (you may need to adjust based on your model)
        dim = 300
        index = IndexFlat(dim, IndexFlat.L2)
        
        # Create list of embeddings from memories
        # Note: This is simplified and you'll need a proper embedding function
        embeddings = []
        for memory in self.memories:
            embedding = self._compute_embedding(memory.content)
            embeddings.append(embedding)
            
        # Convert to numpy array
        embeddings_np = np.array(embeddings, dtype=np.float32)
        
        # Add all vectors to index
        index.add(embeddings_np)
        
        self.vector_index = VectorStoreIndex(index)
    
    def _compute_embedding(self, text: str) -> List[float]:
        """Simplified embedding computation (you should replace with actual model)"""
        # This is a placeholder - you should implement proper embedding
        # For example using sentence-transformers or other models
        return [0.1] * 300
    
    def _convert_to_list_of_dicts(self):
        """Helper to convert memories to list of dicts for processing"""
        return [{
            'content': m.content,
            'metadata': m.metadata
        } for m in self.memories]

# Initialize the memory system when module is loaded
memory_system = LongTermMemory()

if __name__ == "__main__":
    # Example usage
    print("Long term memory system initialized.")