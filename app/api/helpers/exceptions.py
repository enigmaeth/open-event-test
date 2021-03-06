from flask_rest_jsonapi.exceptions import JsonApiException


class UnprocessableEntity(JsonApiException):
    title = "Unprocessable Entity"
    status = 422


class ConflictException(JsonApiException):
    title = "Conflict"
    status = 409
