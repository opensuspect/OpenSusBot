import os

# Get discord secret key from environment variable
DISCORD_KEY = os.environ.get('DISCORD_KEY')
if DISCORD_KEY is None:
    raise("No discord key supplied")

def main():
    # Main entry
