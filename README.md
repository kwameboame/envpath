# Envpath

Envpath is a command line utility for saving and retrieving your development environments and paths.


## Features
  - Save your development environment and path
  - Open saved environments and their paths from any directory


## Usage
This tool has only been tested on Windows.

There are currently only two commands available.

#### 1) Saving an env
If you want to save a virtual environment, make sure you are in the working directory of that project and run the following command (replace **envname** with the name of your environment):

`envpath --save envname`

You can use **-s** instead of **--save**

After running this command, a batch file is saved (envname.bat) with the following command in it `@echo off \ncmd /k "cd {path} && workon {env}"`

#### 2) Opening an env
To open a previously saved environment, just run the following command from any directory or path (replace **envname** with the name of your environment):

`envpath --open envname`

Here too, you can also use **-o** instead of **--open**

This command runs the matching batch file (envname.bat). It replaces `cd path/to/project/directory && workon EnvName`



## Requirements & Dependencies
This package depends on the following python packages and will install them if you don't already have them installed:

* **[virtualenv](https://github.com/pypa/virtualenv)** - Virtual Python Environment builder
* **Argparse**  - Already included in the python standard library from python >= 3.2

Just like these packages, Envpath is also open source software.



## Development
Want to contribute code to this repo? You are welcome to do so.



## Contact the Author
Reach me via:
Email - [Click to send mail](mailto:kwame@soscodesoftware.com)
Twitter [@untamedthinking](https://twitter.com/untamedthinking)



## License
MIT
