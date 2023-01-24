
# System Path Locator

This package that allows you to do an sys.path.append one level above the repository for find the modules correctly when you run it from console.
[Pypi Link](https://pypi.org/project/system-path-locator/0.0.0/)
## Installation

Install ```system-path-locator``` package with pip.


```bash
  pip install system-path-locator
```
##### Usage:
1- Import the package.
```sh
from system_path_locator import locator
```
2- Use the package.
```sh
locator.locate('repo_name')
```

3- The function has returned the worspace value, that contains all the path until your repository.
That can be used for json calls, and other purposes.
```sh
worspace = locator.locate('repo_name')
```
```sh
with open(workspace + r"\automation\data\servers.json") as json_server:
    server_json = json.load(json_server)
```

## Authors

- [@tmorales](https://github.com/moralesveratom)

## License used

[MIT](https://choosealicense.com/licenses/mit/)


## Support

For support, email me moralesveratomas@gmail.com


## Feedback

If you have any feedback, please reach out to me at moralesveratomas@gmail.com


## FAQ

#### What Python version is necessary?

To develop this solution I used the Python 3.10 version.

#### What pip version is necessary to install the package?

Make sure you're using the latest version.

Run ```pip install --upgrade pip``` from console.
