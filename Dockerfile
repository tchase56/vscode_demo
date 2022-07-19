FROM continuumio/miniconda3

# Create the environment using conda
RUN conda install -c anaconda jupyter
RUN conda install -c conda-forge mlflow
RUN conda install -c anaconda scikit-learn
RUN conda install -c anaconda psycopg2
RUN conda install -c anaconda boto3

# Install R
RUN apt-get update && apt-get install -y r-base
RUN R -e "install.packages('tidyverse',dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('lubridate',dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('dbplyr',dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('tsibble',dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('feasts',dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('rjson',dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('logger',dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('optparse',dependencies=TRUE, repos='http://cran.rstudio.com/')"