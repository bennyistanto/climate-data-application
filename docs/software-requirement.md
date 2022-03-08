# Software Requirement

If you encounter a problem, please look for a online solution. The installation and configuration described below is mostly performed using a bash shell on macOS. Windows users will need to install and configure a bash shell in order to follow the usage shown below. Try to use [Windows Subsystem for Linux](#enable-the-windows-subsytem-for-linux) for this purpose.


## macOS/Linux

### Installing software for macOS/Linux

If you are new to using Bash refer to the following lessons with Software Carpentry: [http://swcarpentry.github.io/shell-novice/](http://swcarpentry.github.io/shell-novice/)

#### Homebrew and other package

- If you don't have [**Homebrew**](https://brew.sh), you can install it by pasting below code in your macOS/Linux terminal.

	```bash
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	```

- Install `wget` (for downloading data). Use Hombrew to install it by pasting below code in your macOS terminal.

	```bash
	brew install wget
	```

#### Panoply

- Download and install [Panoply Data Viewer](https://www.giss.nasa.gov/tools/panoply/) from [NASA GISS](https://www.giss.nasa.gov/tools/panoply/download/) on your machine for [macOS](https://www.giss.nasa.gov/tools/panoply/download/PanoplyMacOS-4.12.2.dmg) or [Linux](https://www.giss.nasa.gov/tools/panoply/download/PanoplyJ-4.12.2.zip).

#### Anaconda

- Download and install [Anaconda Python](https://www.anaconda.com/products/individual) on your machine for [macOS](https://repo.anaconda.com/archive/Anaconda3-2020.11-MacOSX-x86_64.pkg) or [Linux](https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh).


## Windows

### Enable the Windows Subsytem for Linux

If you are using Windows machine, it's recomended to follow below step. You will experience an error during SPEI calculation cause by `NCO` if you use standard Windows 10 and not using Windows Subsytem for Linux. 

Guideline below are specific for Windows 10. If you are using Windows Server 2019, please follow [Windows Server Installation Guide](https://docs.microsoft.com/en-us/windows/wsl/install-on-server)
    
Reference: [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

You must first enable the "Windows Subsystem for Linux - WSL" optional feature before installing any Linux distributions on Windows.

### Installing software for Windows

If you have a Bash shell already installed on your Windows OS (e.g. Ubuntu Bash) you can use that for the exercise, but it must be a Bash shell

If you are new to using Bash refer to the following lessons with Software Carpentry: [http://swcarpentry.github.io/shell-novice/](http://swcarpentry.github.io/shell-novice/)

#### Homebrew and other package

- If you don't have [Homebrew](https://brew.sh), you can install it by pasting below code in your WSL Ubuntu terminal.

	```bash
	bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
	```

- Install `wget` (for downloading data). Use Hombrew to install it by pasting below code in your WSL Ubuntu  terminal.

	```bash
	brew install wget
	```

#### Panoply

- Download and install [Panoply Data Viewer](https://www.giss.nasa.gov/tools/panoply/) from [NASA GISS](https://www.giss.nasa.gov/tools/panoply/download/) on your machine: [Windows](https://www.giss.nasa.gov/tools/panoply/download/PanoplyWin-4.12.2.zip).

#### Anaconda

- Download and install [Anaconda Python](https://www.anaconda.com/products/individual) on your WSL Ubuntu Linux: [Ubuntu Linux on WSL](https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh).

	`climate-indices` python package used for SPEI calculation is rely on [**netCDF Operator (NCO)**](http://nco.sourceforge.net) and pyNCO wrapper sometimes produce an error in Windows. That's the reason why we will use Anaconda for Linux if you are using Windows machine.

- Go to [https://repo.anaconda.com/archive/](https://repo.anaconda.com/archive/) to find the list of Anaconda releases

- Select the release you want. I have a 64-bit computer, so I chose the latest release ending in `x86_64.sh`. If I had a 32-bit computer, I'd select the `x86.sh` version. If you accidentally try to install the wrong one, you'll get a warning in the terminal. I chose `Anaconda3-2020.11-Linux-x86_64.sh`.

- From the terminal run `wget https://repo.anaconda.com/archive/[YOUR VERSION]`. Example: 

	```bash
	wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
	```

- After download process completed, Run the installation script: `bash Anaconda[YOUR VERSION].sh` 

	```bash
	bash Anaconda3-2020.11-Linux-x86_64.sh
	```

- Read the license agreement and follow the prompts to press Return/Enter to accept. Later will follow with question on accept the license terms, type `yes` and Enter. When asks you if you'd like the installer to prepend it to the path, press Return/Enter to confirm the location. Last question will be about initialize Anaconda3, type `yes` then Enter.

- Close the terminal and reopen it to reload .bash configs. It will automatically activate `base` environment.

- Deactivate `base` environment then set to `false` the confirguration of auto activate the `base` environment by typing

	```bash
	conda deactivate && conda config --set auto_activate_base false
	```

- To test that it worked, `which python` in your Terminal. It should print a path that has anaconda in it. Mine is `/home/gost/anaconda3/bin/python`. If it doesn't have anaconda in the path, do the next step.

- Manually add the Anaconda bin folder to your PATH. To do this, I added `"export PATH=/home/gost/anaconda3/bin:$PATH"` to the bottom of my `~/.bashrc` file.

- Optionally install [**Visual Studio Code**](https://code.visualstudio.com) when prompted

#### ArcGIS

- Some analysis also required `arcpy` python package, so you also required to install ArcGIS Desktop or Pro. Follow this giudeline for the Desktop [https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/introduction.htm#](https://desktop.arcgis.com/en/arcmap/latest/get-started/installation-guide/introduction.htm#) and Pro [https://pro.arcgis.com/en/pro-app/latest/get-started/install-and-sign-in-to-arcgis-pro.htm](https://pro.arcgis.com/en/pro-app/latest/get-started/install-and-sign-in-to-arcgis-pro.htm)