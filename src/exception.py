import sys


def error_message_detail(error, error_detail):
    _, _, error_traceback = error_detail.exc_info()
    error_message = f"\n\nThe error occur in file:  {error_traceback.tb_frame.f_code.co_filename}\nAt line: {error_traceback.tb_lineno}\nMessage: {str(error)}"

    return error_message


class CustomExceptionHandling(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomExceptionHandling(e, sys)
