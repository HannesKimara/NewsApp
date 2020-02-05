[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/HannesKimara/NewsApp/blob/master/LICENSE) [![codebeat badge](https://codebeat.co/badges/49da4007-f4c8-4cf1-b584-1254811f472f)](https://codebeat.co/projects/github-com-hanneskimara-newsapp-master)

# News App
Keep up with current news and top headlines in different caategories spanning from politics to sports

## Getting Started
To clone this repository run in a virtual environment
```bash
$ git clone https://github.com/HannesKimara/NewsApp.git
$ cd NewsApp
$ pip install -r requirements.txt
```

Export or set environment variables
On windows powershell run:

```bash
$env:NEWS_API_KEY="<NEWS_API_KEY>"
```

On unix based OS run:
```bash
$ export NEWS_API_KEY="<NEWS_API_KEY>"
```

To start the server run
```bash
$ python manage.py serve
```

Or alternatively configure your API Key in start.sh and run it
Visit the live [link](https://indjournal.herokuapp.com/) here

## Testing
Conduct Unittest by running
`$ python manage.py test`

## Author
This project was created by Hannes Kimara

## Built With
 - Python 3.6
 - Flask 1.1.1
 - Bootstrap 4.3.1

## License
This is licensed under MIT License Copyright(2020) Hannes Kimara



