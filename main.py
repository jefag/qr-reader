
#!/usr/bin/env python3
import cv2
import numpy as np
from qreader import QReader
import functions_framework
from flask import jsonify


def read_qr_code(screenshot_bytes):
    """
    Takes a screenshot of the current page and extracts QR code content.
    Returns the decoded QR code string or None if no QR code is found.
    """

    # Create a numpy array from the bytes buffer
    nparr = np.frombuffer(screenshot_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a QReader instance
    qreader = QReader()

    # Use the detect_and_decode function to get the decoded QR data
    decoded_text = qreader.detect_and_decode(image=image)

    return decoded_text[0]

@functions_framework.http
def qrreader(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
    """
    if not request.data:
        return jsonify({"error": "No image data provided"}), 400
    
    try:
        result = read_qr_code(request.data)
        if result is None:
            return jsonify({"error": "No QR code found"}), 404
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
