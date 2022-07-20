FROM continuumio/miniconda3

# Create the environment using conda
RUN conda install -c anaconda jupyter=1.0.0
RUN conda install -c conda-forge mlflow=1.27.0
RUN conda install -c anaconda scikit-learn=1.0.2
RUN conda install -c anaconda psycopg2=2.8.6
RUN conda install -c anaconda boto3=1.24.28
RUN conda install -c conda-forge matplotlib=3.5.2
RUN conda install -c anaconda seaborn=0.11.2
RUN conda install -c anaconda sqlalchemy=1.4.39

# Install R and some R libraries 
RUN apt-get update && apt-get install -y r-base
RUN R -e "install.packages('remotes', dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "remotes::install_version('tidyverse',dependencies=TRUE, version = '1.3.2', repos='http://cran.rstudio.com/')"
RUN R -e "remotes::install_version('lubridate',dependencies=TRUE, version = '1.8.0', repos='http://cran.rstudio.com/')"
RUN R -e "remotes::install_version('dbplyr',dependencies=TRUE, version = '2.2.1', repos='http://cran.rstudio.com/')"
RUN R -e "remotes::install_version('tsibble',dependencies=TRUE, version = '1.1.1', repos='http://cran.rstudio.com/')"
RUN R -e "remotes::install_version('feasts',dependencies=TRUE, version = '0.2.2', repos='http://cran.rstudio.com/')"
RUN R -e "remotes::install_version('rjson',dependencies=TRUE, version = '0.2.21', repos='http://cran.rstudio.com/')"
RUN R -e "remotes::install_version('logger',dependencies=TRUE, version = '0.2.2', repos='http://cran.rstudio.com/')"
RUN R -e "remotes::install_version('optparse',dependencies=TRUE, version = '1.7.1', repos='http://cran.rstudio.com/')"
RUN R -e "remotes::install_version('languageserver',dependencies=TRUE, version = '0.3.13', repos='http://cran.rstudio.com/')"