# Welcome to the analysis code of the Dona evaluation study! 
This code reproduces the analysis in the paper "Development and Evaluation of Dona, a Privacy-Preserving Donation Platform for Messaging Data from WhatsApp, Facebook and Instagram" by Hakobyan, Hillmann, Martin, Böttinger and Drimalla submitted to Behavior Research Methods. 

The code is written in Python and structured into several Jupyter notebooks. Below you can find instructions on how to obtain the data, set up the environment, and run the analyses. 
## Getting started
### Setup
1. Start by cloning this repository somewhere on your machine.
1. The data of the study is available on Zenodo at [URL](URL). Please download all data and place it in the `data` folder.
1. Next, install conda. Instructions specific to your operating system can be found at the [conda website](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).
1. After conda is set up, open a terminal/shell, navigate to the location where you cloned this repository to and create the Python environment with the command `conda env create -f dona-analysis.yml -n dona-analysis`.
1. With the environment created, activate it using `conda activate dona-analysis`.
1. Lastly, use the command `jupyter lab` to open the IDE that runs the Jupyter notebooks with our analysis code.

### Reproducing the analysis
The code for re-creating the plots and analyses are in the folder `code`. The files and figures resulting from the analyses will be stored in `reports`. 
The notebooks are named following the section labels in the paper and contain a short introduction. You can run the notebooks in any order. 
For questions, please contact: ohakobyan at techfak.uni-bielefeld.de or drimalla at techfak.uni-bielefeld.de 
