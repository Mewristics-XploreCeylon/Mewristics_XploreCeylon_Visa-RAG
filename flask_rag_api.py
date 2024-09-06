# flask_rag_api.py

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.indices.postprocessor import SimilarityPostprocessor
from llama_index.core.response.pprint_utils import pprint_response

# Load environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Set up OpenAI API key
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Load documents and create an index
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents, show_progress=True)

# Set up retriever and postprocessor
retriever = VectorIndexRetriever(index=index, similarity_top_k=4)
postprocessor = SimilarityPostprocessor(similarity_cutoff=0.80)

# Set up the query engine
query_engine = RetrieverQueryEngine(retriever=retriever, node_postprocessors=[postprocessor])

@app.route('/query', methods=['POST'])
def query_rag():
    try:
        # Get the query from the request
        query = request.json.get("query")

        # Query the RAG model
        response = query_engine.query(query)

        # Format the response
        response_text = pprint_response(response, show_source=True)

        return jsonify({
            "query": query,
            "response": response_text
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
