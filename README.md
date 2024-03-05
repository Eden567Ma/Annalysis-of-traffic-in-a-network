# Annalysis-of-traffic-in-a-network



> This project is a Network Traffic Visualizer. It is coded in Python. It allows generating traffic flows that refer to frames exchanged as part of a protocol executed by two machines.

## Archive Contents


This archive contains:
1. The file _visualisateur.py_, the source code of the project
2. The _howto_ file which explains how to run the program.
3. _.txt_ files, which contain either the frames to be analyzed.
4. An Interface that allows visualizing information related to data traffic in a network.



## Execution
### Pre-execution Commands

First, download the archive of this project.
Then navigate to the location of your downloaded archive and unzip it.

You may need to install the PlantUML library
```bash
pip install plantuml
```
To execute the program, simply run the following two commands in the terminal:

```bash
 python visualisateur.py
 napkin_plantuml visualisation.puml visualisation.txt
```
The first command generates a .puml file containing the necessary information to draw the graph.

The second command generates a .txt file containing the flow graph to display.

That's pretty much it for execution in the terminal. The next section contains instructions on how to achieve the same result but in a graphical interface.


> On Windows and MacOS,

You need to import the Tkinter library either directly from the official website if you have a specific IDE or through a method that will be valid for all your IDEs:

```bash
  python3 --version
  pip3 --version
  pip3 install --upgrade pip
  pip3 install tk
```
Alternatively,

```bash
pip3 install tk
pip install pillow
```

Otherwise, you can also use PyCharm:

    1.File
    2.New Project Settup
    3.Settings for New Project
    4.Python Interpreter
    5.Then enter the desired library, in our case it will be Tkinter, well known for designing graphical interfaces.




> On Linux


There's different _distribution_ and _version_ so there's billow some of them, for the better execution you can install or update your version of python to python 3.10 or 3.9 : 


```bash
  python3 --version
  pip3 --version
  pip3 install --upgrade pip
  pip3 install tk
```

Known for the richness of its distributions, there are indeed several commands related to this. They will all be executed in the terminal.

On Fedora :
```bash
 Sudo dnf install python-tk
```

Pour Mint, Debian 
```bash
 sudo apt install python-tkinter
```

Indeed among the libraries that we will also find, PIP better known as PILLOW. The latter is actually used for displaying images and processing different formats.

```bash
 sudo apt install python-pillow
```

## Usage

After running the first command, you will be asked to enter a file to process, please enter a valid text file name. You will also be asked if you want to use a filter, please answer "yes" or "no". If yes, specify the type of filter you want to use, either an IP address filter or a protocol filter, then enter the protocol or IP address to filter.
