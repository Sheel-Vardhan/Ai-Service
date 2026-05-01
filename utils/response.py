def success_response(data, model="llama-3.3-70b"):
    return {
        "status": "success",
        "model_used": model,
        "data": data
    }

def error_response(message):
    return {
        "status": "error",
        "message": message
    }