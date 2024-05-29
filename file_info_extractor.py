from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

def format_date(date):
    return datetime.fromtimestamp(date).strftime('%m/%d/%Y %I:%M %p')
def get_file_info(file_path):
    try:
        # get file stats
        file_stats = os.stat(file_path)

        # pull file information
        file_info = {
            "file_name": os.path.basename(file_path),
            "file_size": file_stats.st_size,
            "creation_time": format_date(file_stats.st_ctime),
            "modification_time": format_date(file_stats.st_mtime),
            "file_path": file_path
        }

        # ID file extension
        if '.' in file_info["file_name"]:
            file_info["file_extension"] = file_info["file_name"].split('.')[-1]
        else:
            file_info["file_extension"] = None

        return file_info 
    
    except Exception as e:
        return {"error": str(e)}

@app.route('/fileinfo', methods=['POST'])
def file_info():
    # check if file path is in the request
    data = request.json 
    if not data or 'file_path' not in data:
        return jsonify({'error': 'No file path given'}), 400

    file_path = data['file_path']

    # get file info and return as JSON  
    file_info = get_file_info(file_path)
    return jsonify(file_info)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
