# CodingGirls - Python Basics For Beginners

## Prerequisite

### Docker

* [Download Docker](https://www.docker.com/community-edition#/download)
* [Docker Get Started](https://docs.docker.com/get-started)
* [Docker Documentation](https://docs.docker.com)

### Python 3

* [Python 3](https://docs.python.org/3)
* [Python Getting Started](https://www.python.org/about/gettingstarted)

### Jupyter

* [Jupyter](https://jupyter.org)

## Local Docker Jupyter

### Setup Jupyter Container

* `docker run -d --name <container-name> -p 8888:8888 jupyter/minimal-notebook start-notebook.sh --NotebookApp.password='sha1:03f78811b049:e461468440cecbd99ac8e79485392dacb44273cb'`
* open `http://localhost:8888` in browser
* login using password - `password`
* upload `index.ipynb`

### Remove Jupyter Container

`docker rm -f <container-name>`

## Jupyter From [Mybinder](https://mybinder.org)

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/wgx731/CodingGirls-Python-Basics)

*NOTE: Mybinder instance may be shared by other users.*

## Contributing

[Pull Requests](https://github.com/wgx731/CodingGirls-Python-Basics/pulls) are most welcome!

## Thanks

**CodingGirls-Python-Basics** © 2016+, [@wgx731]. Released under the [MIT](https://github.com/wgx731/CodingGirls-Python-Basics/blob/master/LICENSE) License.

Authored and maintained by [@wgx731] with help from contributors ([list][contributors]).

> GitHub [@wgx731]

[@wgx731]: https://github.com/wgx731
[contributors]: https://github.com/wgx731/CodingGirls-Python-Basics/contributors

