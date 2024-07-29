import re


def extract_birds(message: str) -> list:
    pattern = r'[\W, _]'
    extracted_birds = re.sub(r'[\W, _]', ' ', message)

    return extracted_birds.split()


