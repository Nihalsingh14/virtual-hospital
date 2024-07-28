from flask import Flask, request, jsonify
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_symptoms():
    data = request.json
    
    # Load the Jupyter notebook
    with open('notebook.ipynb') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Inject the data into the notebook
    nb.cells[0].source = f"data = {data}"

    # Execute the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': '.'}})
    
    # Get the output (assuming the output is in the last cell)
    output = nb.cells[-1].outputs[0]['text']
    
    return jsonify({'output': output.strip().split("\n")})

if __name__ == '__main__':
    app.run(debug=True)



