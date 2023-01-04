def ResponseData(statusCode, success, error, data):
    return {
        "statusCode": statusCode,
        "success": success,
        "error": error,
        "data": data,
    }