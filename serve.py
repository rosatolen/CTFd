import sys
from CTFd import create_app
app = create_app()
app.run(debug=True, host="0.0.0.0", port=int(sys.argv[1]))
