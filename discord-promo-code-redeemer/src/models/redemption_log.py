class RedemptionLog:
    def __init__(self):
        self.successful_attempts = []
        self.failed_attempts = []

    def log_successful_attempt(self, code, server):
        self.successful_attempts.append({"code": code, "server": server})

    def log_failed_attempt(self, code, server, error_message):
        self.failed_attempts.append({"code": code, "server": server, "error_message": error_message})

    def get_successful_attempts(self):
        return self.successful_attempts

    def get_failed_attempts(self):
        return self.failed_attempts