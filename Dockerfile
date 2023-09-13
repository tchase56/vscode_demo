FROM continuumio/miniconda3

# Create the environment using conda
RUN conda install python=3.10.12
RUN conda install -c anaconda jupyter=1.0.0
RUN conda install -c anaconda scikit-learn=1.3.0
RUN conda install -c anaconda sqlalchemy=1.4.39
RUN conda install -c anaconda numpy=1.22
RUN conda install -c anaconda pandas=1.4.3
RUN conda install -c anaconda ipykernel=6.25.0
RUN conda install -c anaconda typing=3.10.0.0
RUN conda install -c conda-forge matplotlib=3.7.2

# Add cloned repository to container
COPY . ./VSCODE_DEMO
