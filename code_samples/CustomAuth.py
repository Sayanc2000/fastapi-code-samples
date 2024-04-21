class CustomAuth:
    def __init__(self, header: str, prefix: str = None, sample_token: str = None):
        self.header = header
        self.prefix = prefix + " " if prefix else ''
        self.sample_token = sample_token
