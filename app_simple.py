from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Font generation API is running",
        "note": "FontForge backend - upload your ZIP to get .TTF"
    })

@app.route('/generate-font', methods=['POST'])
def generate_font():
    """
    Placeholder - will return success message
    In production, this uses FontForge to generate fonts
    """
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        # For now, return a simple message
        # We'll add FontForge processing once basic deployment works
        return jsonify({
            "status": "received",
            "message": "File received successfully",
            "note": "Font generation will be added in next deployment",
            "files_received": request.files['file'].filename
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
