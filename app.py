from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mpesa_callback', methods=['POST'])
def mpesa_callback():
    try:
        # Process the callback data received from M-Pesa
        callback_data = request.get_json()

        # Check if the callback indicates a successful payment
        if callback_data.get("ResultCode") == 0 and callback_data.get("ResultDesc") == "The service request is processed successfully.":
            # Extract relevant information from the callback_data for successful payment
            # (e.g., transaction details, update database, send confirmation email, etc.)
            print("Payment successful!")
        else:
            # Handle unsuccessful payment or any other error
            print("Payment failed or an error occurred:", callback_data.get("ResultDesc"))

        # Respond to M-Pesa with a success message
        response = {
            "ResultCode": 0,
            "ResultDesc": "Callback received successfully"
        }

        return jsonify(response)

    except Exception as e:
        # Handle any exceptions that may occur during callback processing
        print("Error processing callback:", str(e))
        response = {
            "ResultCode": 1,
            "ResultDesc": "Error processing callback"
        }
        return jsonify(response)

if __name__ == '__main__':
    # Run the server on a specific port (e.g., 5000)
    app.run(port=5000)
