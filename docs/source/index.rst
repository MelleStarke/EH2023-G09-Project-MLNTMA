Network traffic monitoring techinques using Machine Learning
============================================================

Welcome. This is a collection of resources that can help one start with using Machine Learning in the field of Network Traffic Analysis. We hope that people find this resource useful. We provide explanations and code of some of the popular ML and DL algorithms in order to provide readers with inspiration on how to use such models in our domain. The documentation is layed out as follows:

.. datasets/gen_dataset
.. toctree::
   :maxdepth: 3

   notebooks/analysis3
   notebooks/analysis_rnn2

In recent years AI and ML have exploded in terms of their popularity, effectiveness and
applicability. Despite cyber-security being increasingly more important in modern days’ digitized
landscape and requiring continuous adaptation to new threats and technologies, the academic
overlap between these fields is surprisingly small. We therefore believe that the advancements
in ML could aid the development of cybersecurity, and to this end, we aim to provide a resource
that details the current state-of-the-art in the field by presenting it in a user-friendly and practical
manner.
For our final project we are going to develop a practical review and guide of current practices in
detecting suspicious network traffic using machine learning. The nature of our work will thus be
education-based, with the aim of providing two perspectives on understanding network traffic in
a documentation-style format: the first component is to provide an overview of the academic
literature and the second component is to provide practical examples in our blog with code
demonstrating how different algorithms are used to classify malicious traffic.Below we provide
some preliminary research on machine learning practices in classifying network traffic.
Academic Literature on Traffic Monitoring
AI is currently being used for different tasks within the domain of Cybersecurity. One such
domain is Online machine learning (OL) and is concerned with the employment of traditional
machine learning algorithms for classifying network traffic (Shahraki, 2022). Such methods are
used for Network Traffic Monitoring and Analysis (NTMA) and are developed to also
accommodate time-dependent online data analysis that is required considering today’s fast
network traffic. OL refers to receiving the data continuously as opposed to offline learning where
all data are available prior to training.
Considering the vast amount of network traffic and data flow on the internet in modern times,
internet traffic classification plays a significant role in the network security domain (Shahraki,
2022). Importantly, the introduction of new and unobserved data means that the underlying data
distribution is dynamic or non-stationary–a concept called concept drift. Typical classifiers
utilized are tree-based models and ensembles. One of the resulting caveats in supervised
learning, is that it implies that the dataset provided should be sufficiently large in order to learn
to represent all possible threats sufficiently (Divakaran et al., 2015). Moreover, trained classifiers
should not only be accurate but also efficient, as the emergence of new threats in network
vulnerabilities is continuous.
Shahraki et al. (2022) emphasize the critical nature of OL to keep up with the current magnitude
and speed of network data, as traditional offline learning of limited utility. That is, the dataset
used for training does not dynamically adapt to incoming streams of data. Taking into account
this problem, Divakaran et al. (2015) devised the Self-Learning Intelligent Classifier (SLIC)
algorithm, that dynamically adapts to continuous incoming traffic such that the model
performance is not compromised by unseen data. SLIC has been reported to outperform
traditional classifiers including K-Nearest Neighbors.
Furthermore, unlike in offline learning where practitioners can easily perform data augmentation
for unbalanced classes and assess model performance, in the context of OL class imbalance is
not as thoroughly studied (Shahraki et al., 2022). This poses a significant challenge when
attempting to detect incoming network traffic, because the distribution of data (and thereby the
classes) are non-static. This makes the task of identifying the under-represented classes
challenging.
Previous work has proposed to alleviate class imbalance using the importance sampling
technique (Wu et al., 2014), where one obtains samples from the minority class and applies a
weighting scheme that attaches more importance to the underrepresented class. This makes
the representation in the classifier equal to the majority class. Other techniques have focused
on generating synthetic samples using SMOTE (Synthetic Minority Over-sampling Technique)
and the Learn++.NIE algorithm that introduces penalties for incorrectly classified samples using
a weighting system (Ditzler & Polikar, 2012).
References
Shahraki, A., Abbasi, M., Taherkordi, A., & Jurcut, A. D. (2022). A comparative study on online
machine learning techniques for network traffic streams analysis. Computer Networks, 207,
108836.
Divakaran, D. M., Su, L., Liau, Y. S., & Thing, V. L. (2015). SLIC: Self-learning intelligent
classifier for network traffic. Computer Networks, 91, 283-297.
Wu, K., Edwards, A., Fan, W., Gao, J., & Zhang, K. (2014, April). Classifying imbalanced data
streams via dynamic feature group weighting with importance sampling. In Proceedings of the
2014 SIAM international conference on data mining (pp. 722-730). Society for Industrial and
Applied Mathematics.
Ditzler, G., & Polikar, R. (2012). Incremental learning of concept drift from streaming imbalanced
data. IEEE transactions on knowledge and data engineering, 25(10), 2283-2301.
Objectives
Our primary objective is to provide our peers with a resource that structures and highlights the
relatively underdeveloped field of ML-based NTMA. We aim to identify, categorize, and evaluate
the range of machine learning algorithms that have been applied in this field. Our focus includes
an assessment of the effectiveness, accuracy, and practicality of these algorithms in real-world
scenarios. Our focus includes an assessment of the effectiveness, accuracy, and practicality of
these algorithms in real-world scenarios.
We aim to structure this information in an accessible and easily digestible format, by structuring
it similarly to code documentation, which our users will be very familiar with. Furthermore,
wherever possible, we want to give our users practical experience by providing example code,
as well as a broad understanding of the available methods through comparative analysis.
   




