# ChatBot Test Script
- This chatbot test script used the [ChatterBot](https://github.com/gunthercox/ChatterBot) framework to build it
- There have few step needed to follow:
-   ```shell
    python -m venv venv
    venv\Script\activate
    python -m pip install chatterbot
    python -m pip install pytz
    ```
- There have one place need to change the python method which on file `venv\Lib\site-packages\sqlalchemy\util\compat.py` line 264 change `time_func = time.clock` to `time_func = time.perf_counter()`