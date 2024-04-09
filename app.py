from controller.youtube_search import app
import threading
from async_controller.async_youtube_search import start_background_task

if __name__ == '__main__':
    threading.Thread(target=start_background_task, daemon=True).start()
    app.run(host='0.0.0.0', debug=True)