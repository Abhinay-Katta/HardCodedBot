# HardCodedBot
### Previously called as NoobBot
### Made using PyQt6 and app compiled with Pyinstaller
 
A voice assistant written in Python and PyQt6 that allows you to perform tasks using voice commands. The application initially started as a simple Python script and later a GUI was added with PyQt6. The application can be compiled using PyInstaller and it plays a GIF while assisting you with voice commands. More commands will be added in the future and development is still in progress.

## Installation
1. Clone the repository:
  ```
  git clone https://github.com/Abhinay-Katta/HardCodedBot
  ```
2. Install the necessary dependencies by running
 ```
 pip install -r requirements.txt
 ```
3. Compile the application using PyInstaller:
 ``` run the install.sh file```
4. Edit the ```.spec``` file according to your wish.
5. Run the command to build from the ```.spec``` file :
```
pyinstaller noobBot.spec
```

## Usage
To use the voice assistant, run the compiled executable named ```noobBot.exe``` from ```app/dist/noobBot``` folder or run the Python script
from the command line: 
```
python main.py
```
### Todo:
- [x] Fix the multiple instance error.
- [ ] Fix the run loop error.
- [ ] Fix the closeEvent error.
- [ ] Add take command funtionality.
- [ ] Add more functionalities.
## Contributing
Contributions are welcome! Please open a pull request with your changes.

## License
This project is licensed under the MIT License, I think.