## Improving model performance:

### Model centric Way:
1) Network Architecture: We would suggest the use of wider/deeper networks with transformers/attention based mechanism, given their success
                         across different sequential tasks. If enabled with more compute. We would like to larger whisper models.
2) Hyperparameter: Bigger batches mean the model processes data faster during training, helping it converge quicker. However, we don't want to
                   rush things and hit just any local optimum. Different optima have different precision levels, so adjusting the batch
                   size helps us find the sweet spot with the best system performance. Starting with a larger batch size early on for speedy convergence,
                   and then dialing it down later for more accuracy and better overall performance.
                   Next on our list is tweaking the learning rate. A bigger learning rate speeds up convergence and helps the model escape local optima
                   but it also makes the system swing around a larger area near the optimal value. On the flip side, a smaller learning rate slows things down and
                   might get stuck in a local optimum, but it brings better convergence accuracy. So, to get the best of both worlds, we're planning to dynamically adjust the learning rate.
                   We'll kick off with a bigger rate for a quick start, then ease into a smaller rate as we get closer to the optimal point.

### Data centric Way:
1) Data Augmentation: Perturbing an audio file with noise or overlapping multiple audios might also benefit us. Masking Frequency might also lead
                      to interesting results.

2) Adding Meta-training tasks: For exmaple predicting the fequency of the audio and other meta tasks surrounding an audio file might affect it densely.


   
