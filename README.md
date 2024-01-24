# Advanced Selector
Has the ability to use multiple selection types:
- Single select
- Multiple selection

## Cross platform implementation

The library make use of the `getch` lib on Linux and `msvcrt` on Windows

## Try it!

### Windows

Make sure to have [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/download/win) installed.

Open a powershell and run:

```ps1
# Clone the repository
git clone https://github.com/kougen/py-advanced-selector

# Change dir
cd py-advanced-selector

# Create a virtual env
py -m venv venv

# Enter the venv
./venv/Scripts/activate

# Install the dependencies
pip install -r requirements.txt

# Start the sample.py
py test\sample.py
```
