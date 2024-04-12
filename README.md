This tool is designed for security testing purposes to identify accessible directories or paths on a web server by attempting to access them with common directory names. 
It performs HTTP GET requests to the specified target website and checks the responses against a user-defined list of valid HTTP status codes.
To start use: git clone https://github.com/Charbelghanime/directorybuster.git
To access the help manual: python3 directorybuster.py -h or python3 directorybuster.py --help
After successful installation use: cd directorybuster
To have all the requirements use: pip install -r requirements.txt
To perform a scan use: python3 directorybuster.py example.com
In the example above, directorybuster.py will automatically use the wordlist /usr/share/wordlists/dirb/common.txt and will show the default status codes: 200, 301, 302, 400, 403, 500, 502. 
Other example:
python3 directorybuster.py example.com -c 200,301,302 -w /usr/share/wordlists/dirb/big.txt
In this example we are using the tool to show only status codes:200,301,302 and we are using the wordlist: /usr/share/wordlists/dirb/big.txt
For more options and detailed usage instructions, refer to the help manual:
    ```sh
    pip install -r requirements.txt
    ```
