from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read paths from environment variables
base_dir = os.getenv('BASE_DIR')
templates_folder = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=templates_folder)

from app import routes
