import sys
from src.logger import logging


def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message[{error}]"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail=None):
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        if self.error_detail:
            return f"{self.error_message}: {self.error_detail}"
        else:
            return self.error_message