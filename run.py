import os
from myapp import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=os.environ.get('PORT'),
        debug=True
    )
