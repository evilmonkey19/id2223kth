# ID2223 - Scalable Machine Learning and Deep Learning

## Group 5 - Members
- Jayesh Vasudeva [0tist](https://github.com/0tist/)
- Enric Perpinyà [evilmonkey19](https://github.com/evilmonkey19/)

## Project 1 - Iris & Wine prediction

Both projects are hosted on HuggingFace:
- [Iris](https://huggingface.co/spaces/ID2223/iris)
- [Iris-monitor](https://huggingface.co/spaces/ID2223/iris-monitor)
- [Wine](https://huggingface.co/spaces/ID2223/wine)
- [Wine-monitor](https://huggingface.co/spaces/ID2223/wine-monitoring)

For both cases there are done using HopsWorks.com, Modal.com and HuggingFace.co.

Under the lab1 you can find both projects: iris & wine. They are structured the same way. Let's examplify the iris project.

The following 2 files are made using jupyter notebooks:

- iris-eda-and-backfill-feature-group.ipynb create the feature group and backfill it with data.

- iris-training-pipeline.ipynb train the model and save it.

The following 2 files are made using python scripts and deployed as pipelines in modal.com:

- iris-feature-pipeline-daily.py do a new flower each day and save it in the feature store.

- iris-batch-inference-pipeline.py do the batch inference and save the results in the feature store.

The HuggingFace-spaces folder contains the files to deploy the model in HuggingFace.co:

- huggingface-spaces-iris is the folder to deploy the model in HuggingFace.co and make the predictions.

- huggingface-spaces-iris-monitor is the folder to deploy the model in HuggingFace.co and make the monitoring of the predictions in the pipeline feature daily.

For the wine project is quite similar the structure.


## Project 1 - Iris & Wine prediction

[Whisper-Soundcloud](https://huggingface.co/spaces/ID2223/whisper-soundcloud)
[Whisper-Online](https://huggingface.co/spaces/ID2223/whisper-online)
