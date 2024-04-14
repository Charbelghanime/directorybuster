<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Buster Usage</title>
</head>
<body>
    <pre id="directoryBusterText">
        ___.                   __                
        \_ |__  __ __  _______/  |_  ___________ 
        | __ \|  |  \/  ___/\   __\/ __ \_  __ \\
        | \_\ \  |  /\___ \  |  | \  ___/|  | \/
        |___  /____//____  > |__|  \___  >__|   
            \/           \/            \/          By Charbel Ghanime

        This tool is designed for security testing purposes to identify accessible directories or paths on a web server by attempting to access them with common directory names.

        To start use: 
        git clone https://github.com/Charbelghanime/directorybuster.git

        After successful installation use: 
        cd directorybuster 

        To have all the requirements installed use:
        pip install -r requirements.txt 

        To access the help manual: 
        ``` 
        python3 directorybuster.py -h
        ``` 
        or 
        ``` 
        python3 directorybuster.py --help 
        ``` 

        To perform a simple scan use: 
        ``` 
        python3 directorybuster.py example.com 
        ``` 

        In the example above, directorybuster.py will automatically use the wordlist /usr/share/wordlists/dirb/common.txt 
        and will show the default status codes: 200, 301, 302, 400, 403, 500, 502. 

        Other example: 
        ``` 
        python3 directorybuster.py example.com -c 200,301,302 -w /usr/share/wordlists/dirb/big.txt 
        ``` 

        In this example we are using the tool to show only status codes:200,301,302 and we are using the wordlist: /usr/share/wordlists/dirb/big.txt 

        For more options and detailed usage instructions, refer to the help manual: 
        ``` 
        python3 directorybuster.py -h 
        ``` 

        Contributions to Directory Buster are welcome! If you encounter bugs, have suggestions for new features, or want to contribute improvements, please open an issue or submit a pull request on the GitHub repository.

        This project is licensed under the MIT License - see the LICENSE file for details.
    </pre>

    <button id="copyButton">Copy</button>

    <script>
        document.getElementById('copyButton').addEventListener('click', function() {
            var textToCopy = document.getElementById('directoryBusterText').innerText;
            navigator.clipboard.writeText(textToCopy).then(function() {
                alert('Text copied to clipboard');
            }, function(err) {
                console.error('Failed to copy text: ', err);
            });
        });
    </script>
</body>
</html>
